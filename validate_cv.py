import argparse
import re
import sys
from pathlib import Path
from typing import cast

from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import ViewportSize
from playwright.sync_api import sync_playwright


DEFAULT_SELECTORS = [
    "#cv-root",
    ".cv-hero",
    ".cv-name",
    ".cv-photo",
    "#experience-section",
    ".experience-table",
    "#certifications-section",
    ".cert-grid",
    "#contact-section",
    ".contact-card",
]

DEFAULT_EVIDENCE_DIR = Path(".sisyphus/evidence/validate_cv")
DESKTOP_VIEWPORT = {"width": 1440, "height": 1600}
MOBILE_VIEWPORT = {"width": 390, "height": 844}


class ValidationError(Exception):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate the local CV HTML, screenshots, and PDF export."
    )
    parser.add_argument(
        "--input",
        default="index.html",
        help="Path to the HTML file to validate (default: index.html)",
    )
    parser.add_argument(
        "--evidence-dir",
        default=str(DEFAULT_EVIDENCE_DIR),
        help="Directory for screenshots and PDF evidence",
    )
    parser.add_argument(
        "--require-selector",
        action="append",
        default=[],
        help="Additional selector that must exist exactly once; repeatable",
    )
    parser.add_argument(
        "--print-only",
        action="store_true",
        help="Only run PDF export validation",
    )
    return parser.parse_args()


def ensure_input_file(input_path: Path) -> Path:
    resolved = input_path.resolve()
    if not resolved.exists():
        raise ValidationError(f"Input HTML file not found: {input_path}")
    if resolved.is_dir():
        raise ValidationError(
            f"Input path must be a file, not a directory: {input_path}"
        )
    return resolved


def make_file_url(path: Path) -> str:
    return path.resolve().as_uri()


def ensure_evidence_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path.resolve()


def assert_required_selectors(page, selectors: list[str]) -> None:
    for selector in selectors:
        count = page.locator(selector).count()
        if count != 1:
            raise ValidationError(
                f"Selector validation failed for '{selector}': expected 1 match, found {count}"
            )


def assert_images_loaded(page) -> None:
    image_state = page.locator("img").evaluate_all(
        """
        images => images.map(img => ({
            src: img.getAttribute('src') || '',
            alt: img.getAttribute('alt') || '',
            complete: img.complete,
            naturalWidth: img.naturalWidth,
        }))
        """
    )

    if not image_state:
        raise ValidationError("No <img> elements found to validate")

    failed = [
        image
        for image in image_state
        if not image["complete"] or image["naturalWidth"] <= 0
    ]
    if failed:
        details = ", ".join(
            f"src='{image['src']}' alt='{image['alt']}' complete={image['complete']} naturalWidth={image['naturalWidth']}"
            for image in failed
        )
        raise ValidationError(f"Image validation failed: {details}")


def assert_meaningful_alt_text(page) -> None:
    image_state = page.locator("img").evaluate_all(
        """
        images => images.map(img => ({
            src: img.getAttribute('src') || '',
            alt: (img.getAttribute('alt') || '').trim(),
        }))
        """
    )

    missing_alt = [image for image in image_state if not image["alt"]]
    if missing_alt:
        details = ", ".join(f"src='{image['src']}'" for image in missing_alt)
        raise ValidationError(f"Missing non-empty alt text for images: {details}")


def assert_local_assets_exist(input_path: Path, page) -> None:
    asset_state = page.locator("img[src], link[href][rel='stylesheet']").evaluate_all(
        """
        nodes => nodes.map(node => ({
            tag: node.tagName.toLowerCase(),
            attr: node.tagName.toLowerCase() === 'img' ? 'src' : 'href',
            value: node.getAttribute(node.tagName.toLowerCase() === 'img' ? 'src' : 'href') || '',
        }))
        """
    )

    missing = []
    for asset in asset_state:
        value = asset["value"].strip()
        if not value or "://" in value or value.startswith("data:"):
            continue
        asset_path = (input_path.parent / value).resolve()
        if not asset_path.exists():
            missing.append(f"{asset['tag']} {asset['attr']}='{value}'")

    if missing:
        raise ValidationError("Broken local asset path(s): " + ", ".join(missing))


def capture_screenshot(
    browser, file_url: str, viewport: dict, output_path: Path
) -> None:
    page = browser.new_page(
        viewport=cast(ViewportSize, viewport), device_scale_factor=1
    )
    try:
        page.goto(file_url)
        page.wait_for_load_state("networkidle")
        page.screenshot(path=str(output_path), full_page=True)
    finally:
        page.close()


def export_pdf(browser, file_url: str, output_path: Path) -> None:
    page = browser.new_page()
    try:
        page.goto(file_url)
        page.wait_for_load_state("networkidle")
        page.pdf(
            path=str(output_path),
            format="A4",
            prefer_css_page_size=True,
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
    finally:
        page.close()

    if not output_path.exists() or output_path.stat().st_size <= 0:
        raise ValidationError(
            f"PDF export failed or produced an empty file: {output_path}"
        )

    page_count = len(re.findall(rb"/Type\s*/Page\b", output_path.read_bytes()))
    if page_count != 1:
        raise ValidationError(
            f"PDF export must contain exactly 1 page, found {page_count}: {output_path}"
        )


def validate(
    input_path: Path, evidence_dir: Path, selectors: list[str], print_only: bool
) -> None:
    resolved_input = ensure_input_file(input_path)
    resolved_evidence_dir = ensure_evidence_dir(evidence_dir)
    file_url = make_file_url(resolved_input)
    pdf_path = resolved_evidence_dir / f"{resolved_input.stem}.pdf"

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        try:
            if not print_only:
                page = browser.new_page(
                    viewport=cast(ViewportSize, DESKTOP_VIEWPORT), device_scale_factor=1
                )
                try:
                    page.goto(file_url)
                    page.wait_for_load_state("networkidle")
                    assert_required_selectors(page, selectors)
                    assert_local_assets_exist(resolved_input, page)
                    assert_images_loaded(page)
                    assert_meaningful_alt_text(page)
                finally:
                    page.close()

                capture_screenshot(
                    browser,
                    file_url,
                    DESKTOP_VIEWPORT,
                    resolved_evidence_dir / "desktop.png",
                )
                capture_screenshot(
                    browser,
                    file_url,
                    MOBILE_VIEWPORT,
                    resolved_evidence_dir / "mobile.png",
                )

            export_pdf(browser, file_url, pdf_path)
        finally:
            browser.close()


def main() -> int:
    args = parse_args()
    selectors = [*DEFAULT_SELECTORS, *args.require_selector]

    try:
        validate(
            input_path=Path(args.input),
            evidence_dir=Path(args.evidence_dir),
            selectors=selectors,
            print_only=args.print_only,
        )
    except ValidationError as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1
    except PlaywrightError as exc:
        print(f"Playwright validation error: {exc}", file=sys.stderr)
        return 2
    except Exception as exc:
        print(f"Unexpected validation error: {exc}", file=sys.stderr)
        return 3

    if args.print_only:
        print("Validation passed. Print smoke passed.")
    else:
        evidence_dir = Path(args.evidence_dir)
        pdf_name = f"{Path(args.input).stem}.pdf"
        print(
            "Validation passed. Evidence: "
            f"{evidence_dir / 'desktop.png'}, {evidence_dir / 'mobile.png'}, {evidence_dir / pdf_name}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
