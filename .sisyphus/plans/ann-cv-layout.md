# ANN Premium CV — HTML/CSS + Desktop/Mobile/Print

## TL;DR
> **Summary**: Build a single static HTML/CSS CV for ANN that modernizes the dark-gold luxury poster reference into a cleaner editorial layout while preserving the premium tone. The same DOM must support desktop browsing, phone browsing, and a single-page A4 PDF export through `export_cv.py`.
> **Deliverables**:
> - `index.html` with semantic CV structure and deterministic selectors
> - `styles.css` with shared design tokens, desktop/mobile rules, and strict print rules
> - `validate_cv.py` lightweight post-implementation verification harness
> - A working `python3 export_cv.py index.html` flow producing a one-page A4 PDF
> **Effort**: Medium
> **Parallel**: YES - 2 waves
> **Critical Path**: Task 1 → Task 2 → Task 4 → Task 6 → Task 9 → Task 10

## Context
### Original Request
Create an HTML/CSS CV using `cv.md` as the text source, `IMG_6567 2.png` as the visual reference, the certification icons in `images/`, and `ann_trx.png` as the profile photo. Research modern beautiful CV patterns and support 3 layouts: desktop web, mobile-responsive, and single-page A4 print/PDF via `export_cv.py`.

### Interview Summary
- Visual direction: modernized homage, not a literal clone
- Mobile priority: readability first while preserving the premium identity
- Profile photo: include `ann_trx.png`
- Print style: keep the dark luxury look in the PDF
- Test strategy: tests-after setup plus agent-executed QA

### Metis Review (gaps addressed)
- Locked the overflow policy: when print content is too tall, reduce decorative spacing first, then reduce non-critical ornament size, then reduce print typography to the defined floor; do not remove core content
- Locked font strategy: default to local/system-safe luxury serif + sans stacks to keep `file://` export deterministic and avoid dependency drift
- Locked asset policy: use existing local assets directly; do not rename source files unless a broken path forces it
- Locked scope boundary: acceptance target is browser rendering + exported PDF appearance, not calibrated physical printer output

## Work Objectives
### Core Objective
Produce a premium, polished CV page that reads beautifully on desktop and mobile while exporting reliably to a single A4 PDF page with no clipped content, no missing assets, and no dependence on manual edits before export.

### Deliverables
- Static `index.html`
- Static `styles.css`
- Lightweight `validate_cv.py`
- Working PDF export using existing `export_cv.py`

### Definition of Done (verifiable conditions with commands)
- `python3 export_cv.py index.html` exits `0` and creates `index.pdf`
- `index.html` loads locally via `file://` with all six certification icons and `ann_trx.png` visible
- At a desktop viewport of `1440x1600`, the page renders as a premium two-column layout with no horizontal scroll
- At a mobile viewport of `390x844`, content stacks into a readable single-column flow with no overlap or clipped text
- In print mode, the exported PDF is one A4 page with the dark-gold styling preserved and no section spilling to page 2
- `validate_cv.py` exits `0` after checking required selectors, image load success, desktop/mobile screenshots, and PDF export smoke

### Must Have
- One shared HTML structure for all three modes
- Dark-charcoal + gold visual system inspired by the reference image
- Top hero area with ANN name, subtitle, and profile photo
- Experience section sourced from `cv.md`
- Certifications section with the six local badge icons
- Contact section sourced from `cv.md`
- Deterministic selectors for QA: `#cv-root`, `.cv-hero`, `.cv-name`, `.cv-photo`, `#experience-section`, `.experience-table`, `#certifications-section`, `.cert-grid`, `#contact-section`, `.contact-card`
- Print-specific rules using `@media print`, `@page`, `mm`, and `pt`

### Must NOT Have (guardrails, AI slop patterns, scope boundaries)
- No JavaScript-driven layout logic
- No theme switcher, animations, sliders, or interactive widgets
- No markdown parser/runtime conversion in the browser
- No external icon library
- No framework, bundler, or CSS framework
- No dependence on remote fonts for core rendering
- No literal pixel-perfect clone of `IMG_6567 2.png`
- No scope expansion into copywriting, logo design, or printer calibration

## Verification Strategy
> ZERO HUMAN INTERVENTION - all verification is agent-executed.
- Test decision: tests-after + lightweight Playwright/Python smoke validation
- QA policy: Every task includes agent-executed happy-path and failure/edge-case scenarios
- Evidence: `.sisyphus/evidence/task-{N}-{slug}.{ext}`
- Desktop verification viewport: `1440x1600`
- Mobile verification viewport: `390x844`
- Print verification command: `python3 export_cv.py index.html`
- Print fit policy: if export overflows, fix in this order only — reduce decorative spacing → reduce non-critical ornament scale → reduce print font sizes down to floor (`h1 16pt`, section heading `10.5pt`, body `8.25pt`) → tighten intra-card gaps. Do not remove core content.

## Execution Strategy
### Parallel Execution Waves
> Target: 5-8 tasks per wave. <3 per wave (except final) = under-splitting.
> Extract shared dependencies as Wave-1 tasks for max parallelism.

Wave 1: content/asset contract, semantic scaffold, section markup, design system base, verification scaffold

Wave 2: desktop composition, module styling, mobile overrides, print tuning, polish/accessibility/final validation

### Dependency Matrix (full, all tasks)
| Task | Depends On | Blocks |
|---|---|---|
| 1 | none | 2, 3, 6, 7 |
| 2 | 1 | 3, 5, 6, 8, 9 |
| 3 | 1, 2 | 6, 8, 9 |
| 4 | 1 | 6, 7, 8, 9, 10 |
| 5 | 2 | 10 |
| 6 | 2, 3, 4 | 8, 9, 10 |
| 7 | 1, 2, 4 | 8, 9, 10 |
| 8 | 4, 6, 7 | 10 |
| 9 | 4, 6, 7 | 10 |
| 10 | 5, 8, 9 | Final verification |

### Agent Dispatch Summary (wave → task count → categories)
- Wave 1 → 5 tasks → `quick`, `visual-engineering`, `unspecified-low`
- Wave 2 → 5 tasks → `visual-engineering`, `deep`, `unspecified-high`

## TODOs
> Implementation + Test = ONE task. Never separate.
> EVERY task MUST have: Agent Profile + Parallelization + QA Scenarios.

- [x] 1. Lock content contract and asset mapping

  **What to do**: Create a deterministic implementation contract from `cv.md` and the local images. Preserve the source copy, normalize it into HTML-ready section data, and map each certification to its exact badge asset: `ACE CPT → images/ace.png`, `TRX-STC Suspension Training → images/trx.png`, `THUMP BOXING Level 1 & 2 → images/box.png`, `Kettlebell Quest IKT Level 1 → images/kettle.png`, `CPR+AED Certification → images/cpr.png`, `Bodyweight Training C-level → images/pesa.png`. Treat `ann_trx.png` as the profile photo and `IMG_6567 2.png` as inspiration only, not as a rendered runtime asset.
  **Must NOT do**: Do not rewrite the copy, rename existing source files, or introduce new imagery.

  **Recommended Agent Profile**:
  - Category: `quick` - Reason: bounded content/asset mapping with no architectural uncertainty
  - Skills: `[]` - no extra skill required
  - Omitted: `frontend-design` - design execution is not needed yet

  **Parallelization**: Can Parallel: YES | Wave 1 | Blocks: 2, 3, 6, 7 | Blocked By: none

  **References** (executor has NO interview context - be exhaustive):
  - Content source: `cv.md:2-30` - canonical copy for name, subtitle, experience, certifications, and contact details
  - Badge assets: `images/ace.png`, `images/trx.png`, `images/box.png`, `images/kettle.png`, `images/cpr.png`, `images/pesa.png` - exact icon files to use
  - Photo: `ann_trx.png` - required profile photo
  - Visual direction: `IMG_6567 2.png` - dark/gold luxury tone and structural inspiration only

  **Acceptance Criteria** (agent-executable only):
  - [ ] A written asset/content mapping exists in implementation comments, constants, or task notes before styling begins
  - [ ] All six certifications from `cv.md` have a one-to-one rendered asset mapping with no omissions
  - [ ] No runtime dependency on `IMG_6567 2.png` exists in the final HTML

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```
  Scenario: Asset contract is complete
    Tool: Bash
    Steps: Run `python3 - <<'PY'
from pathlib import Path
required = [
    'images/ace.png','images/trx.png','images/box.png','images/kettle.png','images/cpr.png','images/pesa.png','ann_trx.png','cv.md'
]
missing = [p for p in required if not Path(p).exists()]
print('MISSING', missing)
raise SystemExit(1 if missing else 0)
PY`
    Expected: Exit code 0 and `MISSING []`
    Evidence: .sisyphus/evidence/task-1-content-contract.txt

  Scenario: Missing asset is detected
    Tool: Bash
    Steps: Run the same script with one required path temporarily edited to `images/not-real.png`
    Expected: Non-zero exit and missing-path output
    Evidence: .sisyphus/evidence/task-1-content-contract-error.txt
  ```

  **Commit**: NO | Message: `n/a` | Files: `cv.md`, `images/*.png`, `ann_trx.png`

- [x] 2. Build semantic HTML scaffold and deterministic selectors

  **What to do**: Create `index.html` as the single entry file expected by `export_cv.py`. Use semantic sections and deterministic selectors: `#cv-root`, `.cv-hero`, `.cv-name`, `.cv-subtitle`, `.cv-photo`, `#experience-section`, `.experience-table`, `#certifications-section`, `.cert-grid`, `#contact-section`, `.contact-card`. Structure the DOM as: page wrapper → hero block → content grid → main experience column + right-side certifications/contact column. Ensure the hero contains the ANN name, subtitle, and photo.
  **Must NOT do**: Do not use div soup, JavaScript rendering, or duplicate DOM branches per viewport.

  **Recommended Agent Profile**:
  - Category: `visual-engineering` - Reason: semantic structure must directly support later layout work
  - Skills: `[]` - keep this task focused on structure
  - Omitted: `frontend-design` - no visual polish yet

  **Parallelization**: Can Parallel: NO | Wave 1 | Blocks: 3, 5, 6, 8, 9 | Blocked By: 1

  **References** (executor has NO interview context - be exhaustive):
  - Export contract: `export_cv.py:6-29` - HTML must be loadable locally and printable to A4 PDF
  - Content source: `cv.md:2-30` - source sections and ordering
  - Photo requirement: `ann_trx.png` - must appear in hero
  - Reference image: `IMG_6567 2.png` - indicates photo prominence and dark-premium hierarchy

  **Acceptance Criteria** (agent-executable only):
  - [ ] `index.html` exists at repo root and opens under `file://`
  - [ ] All required selectors appear exactly once except repeated certification cards inside `.cert-grid`
  - [ ] Experience, certifications, and contact content are present as HTML text sourced from `cv.md`

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```
  Scenario: Semantic scaffold renders locally
    Tool: Playwright
    Steps: Open `file://.../index.html`, query `#cv-root`, `.cv-hero`, `#experience-section`, `#certifications-section`, and `#contact-section`
    Expected: Every selector resolves exactly once and page shows ANN name text
    Evidence: .sisyphus/evidence/task-2-html-scaffold.png

  Scenario: Missing selector fails validation
    Tool: Bash
    Steps: Run `python3 - <<'PY'
from pathlib import Path
html = Path('index.html').read_text(encoding='utf-8')
required = ['#cv-root','.cv-hero','.cv-name','.cv-photo','#experience-section','.experience-table','#certifications-section','.cert-grid','#contact-section','.contact-card']
missing = [s for s in required if s.replace('#','id="').replace('.','class="') not in html and s not in html]
print(missing)
raise SystemExit(1 if missing else 0)
PY`
    Expected: Exit code 0 for the real file; non-zero if one selector token is removed
    Evidence: .sisyphus/evidence/task-2-html-scaffold-error.txt
  ```

  **Commit**: NO | Message: `n/a` | Files: `index.html`

- [x] 3. Encode the experience matrix and section content hierarchy

  **What to do**: Convert the markdown CV content into a screen/print-efficient hierarchy. Keep ANN’s subtitle below the name. Render experience as a two-column table/matrix with left labels and right institution/project lists. Render certifications as six uniform cards with icon + short label + supporting descriptor. Render contact as a compact card with name, email, phone, and teaching specialties. Use concise line breaks for print efficiency but do not remove facts.
  **Must NOT do**: Do not invent new sections, reduce the certification list, or preserve markdown table syntax verbatim in the HTML.

  **Recommended Agent Profile**:
  - Category: `visual-engineering` - Reason: content hierarchy directly affects layout density and readability
  - Skills: `[]` - direct HTML content work only
  - Omitted: `frontend-design` - defer aesthetic execution to later tasks

  **Parallelization**: Can Parallel: YES | Wave 1 | Blocks: 6, 8, 9 | Blocked By: 1, 2

  **References** (executor has NO interview context - be exhaustive):
  - Name/subtitle: `cv.md:2-3`
  - Experience source rows: `cv.md:5-12`
  - Certification source list: `cv.md:15-22`
  - Contact source list: `cv.md:26-30`
  - Reference structure inspiration: `IMG_6567 2.png` - uses strong section segmentation and compact right-column modules

  **Acceptance Criteria** (agent-executable only):
  - [ ] Experience section contains exactly three experience rows sourced from `cv.md`
  - [ ] Certification section contains exactly six cards
  - [ ] Contact card contains email, phone, and specialties with no missing data

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```
  Scenario: Content hierarchy matches source CV
    Tool: Playwright
    Steps: Open `index.html`, count `.experience-row` elements, count `.cert-card` elements, and inspect `#contact-section` text for `ann810613@hotmail.com` and `0980-404-516`
    Expected: Counts are `3` and `6`; contact text includes both email and phone
    Evidence: .sisyphus/evidence/task-3-content-hierarchy.png

  Scenario: Extra or missing content is caught
    Tool: Bash
    Steps: Run `python3 - <<'PY'
from pathlib import Path
html = Path('index.html').read_text(encoding='utf-8')
checks = ['ann810613@hotmail.com','0980-404-516','ACE Certified Personal Trainer','TRX-STC Suspension Training']
missing = [c for c in checks if c not in html]
print(missing)
raise SystemExit(1 if missing else 0)
PY`
    Expected: Exit code 0 for the final file; non-zero if any required content is missing
    Evidence: .sisyphus/evidence/task-3-content-hierarchy-error.txt
  ```

  **Commit**: YES | Message: `feat(cv): add semantic content scaffold` | Files: `index.html`

- [x] 4. Establish the shared CSS design system and screen-safe typography

  **What to do**: Create `styles.css` with a design-token layer for colors, spacing, radii, borders, and type scale. Use a dark-charcoal base with gold/champagne accents and warm-white text. Use local/system-safe font stacks only: heading stack `"Iowan Old Style", "Palatino Linotype", "Book Antiqua", "Times New Roman", serif`; body stack `"Avenir Next", "Segoe UI", "Helvetica Neue", Arial, sans-serif`. Implement fluid screen typography with `clamp()` and shared utility rules for cards, section headings, divider lines, and image treatments.
  **Must NOT do**: Do not import remote fonts, use CSS frameworks, or bake print-only units into screen rules.

  **Recommended Agent Profile**:
  - Category: `visual-engineering` - Reason: tokenized styling is the foundation for all three layouts
  - Skills: [`frontend-design`] - reason: helps enforce a premium dark-luxury direction without generic styling
  - Omitted: `ai-slop-remover` - premature for first-pass styling

  **Parallelization**: Can Parallel: YES | Wave 1 | Blocks: 6, 7, 8, 9, 10 | Blocked By: 1

  **References** (executor has NO interview context - be exhaustive):
  - Reference image: `IMG_6567 2.png` - dark slate background, gold borders, strong typography contrast
  - Modern CSS fluid typography: `https://modern-css.com/fluid-typography-without-media-queries`
  - Content source for text density: `cv.md:2-30`

  **Acceptance Criteria** (agent-executable only):
  - [ ] `styles.css` defines reusable CSS custom properties for colors, spacing, and type scale
  - [ ] Headings and body text use the approved local/system-safe font stacks only
  - [ ] Screen typography uses `clamp()` for at least the page title, section headings, and body text

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```
  Scenario: Design tokens load on screen
    Tool: Playwright
    Steps: Open `index.html`, inspect computed styles for `.cv-name`, `body`, and a section card, then capture a screenshot
    Expected: Background is dark, title uses serif stack, body uses sans stack, and gold accent color is visibly applied
    Evidence: .sisyphus/evidence/task-4-design-system.png

  Scenario: Forbidden remote font dependency is absent
    Tool: Bash
    Steps: Run `python3 - <<'PY'
from pathlib import Path
css = Path('styles.css').read_text(encoding='utf-8')
forbidden = ['@import url(','fonts.googleapis.com','use.typekit.net']
hits = [t for t in forbidden if t in css]
print(hits)
raise SystemExit(1 if hits else 0)
PY`
    Expected: Exit code 0 and no forbidden font imports found
    Evidence: .sisyphus/evidence/task-4-design-system-error.txt
  ```

  **Commit**: NO | Message: `n/a` | Files: `styles.css`

- [x] 5. Add a lightweight post-implementation validation harness

  **What to do**: Create `validate_cv.py` using Playwright Python so the repo has a repeatable tests-after validation path. The script must open `index.html` via `file://`, assert the required selectors, verify all local images report successful load state, capture desktop and mobile screenshots, invoke `export_cv.py` or equivalent PDF export logic, and fail if the PDF is missing. Keep it dependency-light and reuse the existing Playwright Python environment implied by `export_cv.py`.
  **Must NOT do**: Do not add a package manager, test framework, snapshot-diff library, or browser-only manual steps.

  **Recommended Agent Profile**:
  - Category: `unspecified-low` - Reason: small support script with constrained scope
  - Skills: `[]` - no specialized skill needed
  - Omitted: `playwright` - this is code creation, not browser-operation-only work

  **Parallelization**: Can Parallel: YES | Wave 1 | Blocks: 10 | Blocked By: 2

  **References** (executor has NO interview context - be exhaustive):
  - Existing export implementation: `export_cv.py:6-48` - reuse its Playwright/PDF assumptions
  - Required selectors from this plan: `#cv-root`, `.cv-hero`, `.cv-name`, `.cv-photo`, `#experience-section`, `.experience-table`, `#certifications-section`, `.cert-grid`, `#contact-section`, `.contact-card`

  **Acceptance Criteria** (agent-executable only):
  - [ ] `validate_cv.py` exits `0` when `index.html`, local assets, and `index.pdf` are generated successfully
  - [ ] The script writes desktop and mobile screenshots to a deterministic local path
  - [ ] The script supports `--print-only` so print export checks can run independently
  - [ ] The script exits non-zero if `index.html` is missing, a required selector is absent, or the PDF is not produced

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```
  Scenario: Validation harness passes on healthy build
    Tool: Bash
    Steps: Run `python3 validate_cv.py`
    Expected: Exit code 0, screenshots created, and `index.pdf` present after execution
    Evidence: .sisyphus/evidence/task-5-validation-harness.txt

  Scenario: Validation harness fails on missing entry file
    Tool: Bash
    Steps: Temporarily point the script at `missing.html` or run a negative test branch inside the script
    Expected: Non-zero exit with a clear missing-file error
    Evidence: .sisyphus/evidence/task-5-validation-harness-error.txt
  ```

  **Commit**: YES | Message: `test(cv): add local validation scaffold` | Files: `validate_cv.py`

- [x] 6. Implement the premium desktop composition

  **What to do**: Build the desktop layout at `min-width: 1024px` as a polished editorial canvas. Use a top hero band with ANN’s name, subtitle, and circular or softly rounded profile photo treatment. Below it, use a two-column body grid with the experience matrix on the left (~60%) and certifications/contact on the right (~40%). Add restrained gold dividers, subtle panel depth, and generous spacing so the result feels premium rather than crowded.
  **Must NOT do**: Do not recreate the poster literally, use neon gold gradients, or let the right column overpower the experience section.

  **Recommended Agent Profile**:
  - Category: `visual-engineering` - Reason: this is the core screen-layout task
  - Skills: [`frontend-design`] - reason: needed to preserve the luxury tone without generic patterns
  - Omitted: `frontend-ui-ux` - not necessary alongside the project skill

  **Parallelization**: Can Parallel: YES | Wave 2 | Blocks: 8, 9, 10 | Blocked By: 2, 3, 4

  **References** (executor has NO interview context - be exhaustive):
  - Reference mood/layout: `IMG_6567 2.png` - hero prominence, left-dominant main content, compact right modules
  - Content structure: `cv.md:2-30`
  - Export constraints that influence spacing density: `export_cv.py:23-29`

  **Acceptance Criteria** (agent-executable only):
  - [ ] At `1440x1600`, the page uses a two-column content grid beneath the hero
  - [ ] Experience matrix is visually dominant over the right rail
  - [ ] No horizontal scrollbar appears on desktop

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```
  Scenario: Desktop composition matches intended hierarchy
    Tool: Playwright
    Steps: Open `index.html` at `1440x1600`, capture a full-page screenshot, and inspect the layout widths of the experience and sidebar columns
    Expected: Two-column layout is visible, experience column is wider than sidebar, and the hero photo is visible above the body grid
    Evidence: .sisyphus/evidence/task-6-desktop-layout.png

  Scenario: Desktop overflow is caught
    Tool: Playwright
    Steps: Open `index.html` at `1440x1600`, evaluate `document.documentElement.scrollWidth > document.documentElement.clientWidth`
    Expected: Result is `false`; any `true` result fails the task
    Evidence: .sisyphus/evidence/task-6-desktop-layout-error.txt
  ```

  **Commit**: NO | Message: `n/a` | Files: `styles.css`, `index.html`

- [x] 7. Style the photo, certification cards, and contact card modules

  **What to do**: Implement the right-rail modules so they feel cohesive and compact. The photo treatment must look premium and integrated into the hero/sidebar system. Certification cards must share equal sizing, icon framing, and text hierarchy. The contact card must surface ANN’s name, email, phone, and teaching specialties in a dense but readable block. Use only the local badge images and keep decorative framing subtler than the content itself.
  **Must NOT do**: Do not mix badge sizes, distort icons, or let the contact panel become visually louder than the page title.

  **Recommended Agent Profile**:
  - Category: `visual-engineering` - Reason: component-level visual polish with strong layout dependency
  - Skills: [`frontend-design`] - reason: needed for premium module detailing
  - Omitted: `ai-slop-remover` - premature before the modules settle

  **Parallelization**: Can Parallel: YES | Wave 2 | Blocks: 8, 9, 10 | Blocked By: 1, 2, 4

  **References** (executor has NO interview context - be exhaustive):
  - Badge assets: `images/ace.png`, `images/trx.png`, `images/box.png`, `images/kettle.png`, `images/cpr.png`, `images/pesa.png`
  - Photo asset: `ann_trx.png`
  - Content source: `cv.md:15-30`
  - Reference image: `IMG_6567 2.png` - circular photo treatment and grouped right-side modules

  **Acceptance Criteria** (agent-executable only):
  - [ ] All six certification cards render with visible icons and labels
  - [ ] The photo renders without distortion and maintains a consistent aspect ratio
  - [ ] The contact card displays email, phone, and specialties without clipping

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```
  Scenario: Module assets render correctly
    Tool: Playwright
    Steps: Open `index.html`, count `.cert-card img` elements, inspect `.cv-photo img` natural dimensions, and capture the right rail
    Expected: Six badge images load, the profile photo has non-zero natural width/height, and contact text is fully visible
    Evidence: .sisyphus/evidence/task-7-modules.png

  Scenario: Broken asset path is surfaced
    Tool: Playwright
    Steps: Evaluate all `img` elements for `complete === true && naturalWidth > 0`
    Expected: Every image passes; any `false` result fails the task and reports the offending `src`
    Evidence: .sisyphus/evidence/task-7-modules-error.txt
  ```

  **Commit**: YES | Message: `feat(cv): add premium desktop modules` | Files: `styles.css`, `index.html`

- [x] 8. Implement the mobile-first readable responsive layout

  **What to do**: Make the shared DOM collapse cleanly for phones using a base single-column flow and a desktop enhancement breakpoint at `1024px`. On mobile (`390x844` target), stack content as hero → experience → certifications → contact. Increase tap-safe spacing between cards, reduce ornamental borders, keep the photo smaller than desktop, and ensure long English lines wrap without overflow. Preserve the premium tone, but prioritize reading speed and scanning clarity.
  **Must NOT do**: Do not create a separate mobile HTML file, hide core sections, or preserve decorative density that causes cramped reading.

  **Recommended Agent Profile**:
  - Category: `visual-engineering` - Reason: responsive adaptation from shared DOM requires careful CSS decisions
  - Skills: [`frontend-design`] - reason: maintain style quality while simplifying density
  - Omitted: `frontend-ui-ux` - unnecessary duplication of design guidance

  **Parallelization**: Can Parallel: NO | Wave 2 | Blocks: 10 | Blocked By: 4, 6, 7

  **References** (executor has NO interview context - be exhaustive):
  - User decision: mobile prioritizes readability first
  - Content density source: `cv.md:2-30`
  - Reference tone only: `IMG_6567 2.png` - preserve mood, not exact structure
  - Modern CSS typography guidance: `https://modern-css.com/fluid-typography-without-media-queries`

  **Acceptance Criteria** (agent-executable only):
  - [ ] At `390x844`, the layout is single-column with no horizontal scroll
  - [ ] Name, subtitle, experience, certifications, and contact are visible in the intended stacked order
  - [ ] Long labels wrap within their cards without text overlap

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```
  Scenario: Mobile layout is readable and complete
    Tool: Playwright
    Steps: Open `index.html` at `390x844`, capture a full-page screenshot, and read the text order from top to bottom
    Expected: Hero appears first, followed by experience, certifications, and contact; no horizontal scrolling occurs
    Evidence: .sisyphus/evidence/task-8-mobile-layout.png

  Scenario: Mobile overflow is caught
    Tool: Playwright
    Steps: Open `index.html` at `390x844`, evaluate `document.documentElement.scrollWidth > document.documentElement.clientWidth`, and inspect the longest certification label block
    Expected: Overflow check is `false` and no certification/contact text visually overlaps
    Evidence: .sisyphus/evidence/task-8-mobile-layout-error.txt
  ```

  **Commit**: YES | Message: `feat(cv): add mobile responsive layout` | Files: `styles.css`

- [x] 9. Tune the print stylesheet for single-page A4 export

  **What to do**: Add `@media print` rules and `@page { size: A4 portrait; margin: 0; }` so the CV exports as a single A4 page with zero browser margins. Use fixed print units (`mm`, `pt`) rather than viewport units. Preserve the dark-luxury palette with exact print color adjustment, constrain the page to `210mm × 297mm`, prevent card splitting with `break-inside: avoid`, and apply the defined fit policy if the first export overflows. Use print-specific type sizes with the floor from this plan.
  **Must NOT do**: Do not rely on `vh`/`vw` in print mode, hide core content to force fit, or accept a two-page export.

  **Recommended Agent Profile**:
  - Category: `deep` - Reason: print layout has the most constraints and the highest failure risk
  - Skills: [`frontend-design`] - reason: keep print aesthetically aligned while compressing density
  - Omitted: `playwright` - browser tooling is for QA, not the CSS implementation itself

  **Parallelization**: Can Parallel: NO | Wave 2 | Blocks: 10 | Blocked By: 4, 6, 7

  **References** (executor has NO interview context - be exhaustive):
  - Export contract: `export_cv.py:23-29` - A4, zero margins, `prefer_css_page_size=True`, `print_background=True`
  - MDN printing guidance: `https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Printing`
  - MDN `@page size`: `https://developer.mozilla.org/en-US/docs/Web/CSS/reference/at-rules/@page/size`
  - MDN `break-inside`: `https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/break-inside`

  **Acceptance Criteria** (agent-executable only):
  - [ ] `python3 export_cv.py index.html` exits `0` and creates `index.pdf`
  - [ ] The PDF export results in exactly one A4 page verified by counting `/Type /Page` objects in the PDF bytes
  - [ ] Print mode preserves dark background, gold accents, and readable contrast without clipped sections

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```
  Scenario: Single-page A4 export succeeds
    Tool: Bash
    Steps: Run `python3 export_cv.py index.html` and then `python3 - <<'PY'
from pathlib import Path
import re
pdf = Path('index.pdf')
data = pdf.read_bytes() if pdf.exists() else b''
pages = len(re.findall(rb'/Type\s*/Page\b', data))
print(pdf.exists(), pdf.stat().st_size if pdf.exists() else 0, pages)
raise SystemExit(0 if pdf.exists() and pdf.stat().st_size > 0 and pages == 1 else 1)
PY`
    Expected: Export exits 0, a non-empty `index.pdf` is created, and the page count check returns `1`
    Evidence: .sisyphus/evidence/task-9-print-export.txt

  Scenario: Print overflow or missing PDF is caught
    Tool: Bash
    Steps: Run `python3 validate_cv.py --print-only` or equivalent and fail if the generated PDF is absent, multi-page, or the export command exits non-zero
    Expected: Non-zero exit when print generation fails or overflows beyond one page
    Evidence: .sisyphus/evidence/task-9-print-export-error.txt
  ```

  **Commit**: YES | Message: `feat(cv): tune single-page A4 export` | Files: `styles.css`, `index.html`

- [x] 10. Polish accessibility, contrast, and final validation outputs

  **What to do**: Perform the final pass on readability, semantic quality, and validation tooling. Add alt text to all meaningful images, ensure decorative elements are ignored by assistive tech, confirm heading hierarchy is sensible, tighten any remaining spacing collisions, and update `validate_cv.py` so it captures final desktop/mobile evidence and a print smoke result. Remove dead CSS selectors and ensure local relative paths still work from the repo root under `file://`.
  **Must NOT do**: Do not add new sections, refactor the overall layout concept, or downgrade the visual system to solve small spacing issues.

  **Recommended Agent Profile**:
  - Category: `unspecified-high` - Reason: cross-cutting cleanup and validation across HTML/CSS/script
  - Skills: `[]` - no extra skill required beyond careful execution
  - Omitted: `frontend-design` - polish should refine, not redesign

  **Parallelization**: Can Parallel: NO | Wave 2 | Blocks: Final verification | Blocked By: 5, 8, 9

  **References** (executor has NO interview context - be exhaustive):
  - All source content: `cv.md:2-30`
  - Export logic: `export_cv.py:6-48`
  - Asset set: `images/*.png`, `ann_trx.png`
  - Validation harness from Task 5: `validate_cv.py`

  **Acceptance Criteria** (agent-executable only):
  - [ ] All meaningful images have non-empty alt text; decorative shapes use empty alt or CSS-only rendering
  - [ ] `python3 validate_cv.py` exits `0` and produces desktop/mobile screenshot evidence plus print smoke output
  - [ ] No broken local asset paths remain under `file://` rendering

  **QA Scenarios** (MANDATORY - task incomplete without these):
  ```
  Scenario: Final validation completes successfully
    Tool: Bash
    Steps: Run `python3 validate_cv.py`
    Expected: Exit code 0 with desktop screenshot, mobile screenshot, and print smoke outputs generated
    Evidence: .sisyphus/evidence/task-10-final-polish.txt

  Scenario: Broken alt/path issues are surfaced
    Tool: Playwright
    Steps: Open `index.html`, inspect all `img` nodes for valid `alt` attributes and successful load state, then inspect the accessibility snapshot for logical heading order
    Expected: Every meaningful image has alt text, decorative images are explicitly decorative, and all images load successfully
    Evidence: .sisyphus/evidence/task-10-final-polish-error.txt
  ```

  **Commit**: YES | Message: `chore(cv): polish accessibility and finalize validation` | Files: `index.html`, `styles.css`, `validate_cv.py`

## Final Verification Wave (MANDATORY — after ALL implementation tasks)
> 4 review agents run in PARALLEL. ALL must APPROVE. Present consolidated results to user and get explicit "okay" before completing.
> **Do NOT auto-proceed after verification. Wait for user's explicit approval before marking work complete.**
> **Never mark F1-F4 as checked before getting user's okay.** Rejection or user feedback -> fix -> re-run -> present again -> wait for okay.
- [x] F1. Plan Compliance Audit — oracle
- [x] F2. Code Quality Review — unspecified-high
- [x] F3. Real Manual QA — unspecified-high (+ playwright if UI)
- [x] F4. Scope Fidelity Check — deep

## Commit Strategy
- Commit after Task 3: `feat(cv): add semantic content scaffold`
- Commit after Task 5: `test(cv): add local validation scaffold`
- Commit after Task 7: `feat(cv): add premium desktop modules`
- Commit after Task 8: `feat(cv): add mobile responsive layout`
- Commit after Task 9: `feat(cv): tune single-page A4 export`
- Commit after Task 10: `chore(cv): polish accessibility and finalize validation`

## Success Criteria
- ANN’s CV is visually premium and recognizably inspired by the reference without being a clone
- Desktop, mobile, and print all derive from one HTML/CSS codebase
- PDF export is repeatable and single-page A4 under the existing Playwright export tool
- All required assets load locally with `file://` paths
- Final validation captures screenshots/evidence for desktop, mobile, and exported PDF behavior
