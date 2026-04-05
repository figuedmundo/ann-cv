# ANN Premium CV

A modernized, dark-luxury HTML/CSS CV designed with three distinct layouts from a single codebase:

1. **Desktop Web**: A premium 60/40 two-column editorial composition.
2. **Mobile**: A readability-first, single-column responsive flow.
3. **Print/PDF**: A tailored A4 layout designed to export as a single-page PDF without content clipping.

## Features

* **Single Shared DOM**: No duplicated markup for different viewports.
* **No Javascript for Layout**: The layout relies entirely on CSS Grid, Flexbox, and fluid typography (`clamp()`).
* **System-Safe Typography**: Uses high-quality system font stacks (Iowan Old Style / Palatino for headings; Avenir Next / Segoe UI for body) to ensure fast, deterministic rendering locally without external network dependencies.
* **Premium Aesthetic**: Dark charcoal background with subtle gold/champagne accents, designed as a modernized homage to the original visual concept.
* **Print-Optimized**: Uses `@page` and `@media print` with exact `mm`/`pt` units and `break-inside` controls to guarantee a pristine, single-page A4 PDF export.

## Key Files

* `index.html` — The core semantic HTML structure.
* `styles.css` — The design system containing CSS variables, layout rules, and strict print overrides.
* `export_cv.py` — A Python Playwright script used to export the HTML to a PDF seamlessly.
* `validate_cv.py` — A lightweight Python validation harness to verify structural selectors, local asset loading, image alt text (accessibility), and PDF generation functionality.
* `cv.md` — The original text copy from which the HTML was generated.
* `ann_trx.png` — The profile photo.
* `images/` — Directory containing the 6 required certification badge icons.

## Usage

### 1. View Locally
Simply open the `index.html` file in any modern web browser.
```bash
open index.html
```

### 2. Export to PDF
To generate the exact, single-page A4 PDF (`index.pdf`), run the export script. *(Requires Python 3 and Playwright).*
```bash
python3 export_cv.py index.html
```

### 3. Run Validation
To run the automated validation suite, which checks DOM selectors, tests local asset loading, and performs a smoke test on the PDF export:
```bash
python3 validate_cv.py
```
To run only the PDF/print validation:
```bash
python3 validate_cv.py --print-only
```
