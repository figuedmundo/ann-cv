# Personal Trainer CV - Lin, Ting-An

A professional, print-friendly CV website designed for a Personal Trainer. This project replicates a specific visual design using modern HTML and CSS, featuring a responsive layout that looks great on screens and perfectly formatted on A4 paper for printing.

## 🌟 Features

-   **Professional Design**: High-fidelity replication of a custom design with deep purple aesthetics and gold accents.
-   **Print-Ready**: Optimized CSS ensures the CV utilizes the exact A4 dimensions when printed or saved as PDF.
-   **Responsive**: scales gracefully for viewing on desktop and mobile browsers.
-   **Typography Options**: Includes support for both Modern (Noto Sans TC) and Elegant (Noto Serif TC) Traditional Chinese fonts.
-   **Structured Layout**: distinct sections for Experience, Certifications, and Courses.

## 🛠️ Technologies Used

-   **HTML5**: Semantic structure.
-   **CSS3**: Flexbox for layout, CSS Variables for easy theming, Google Fonts integration.

## 🚀 Getting Started

### Prerequisites
You only need a modern web browser (Chrome, Safari, Firefox, or Edge).

### Installation
1.  **Clone the repository**:
    ```bash
    git clone https://github.com/figuedmundo/ann-cv.git
    ```
2.  **Open the file**:
    Navigate to the project folder and double-click `index.html` to open it in your browser.

## 🎨 Customization

### Content
Edit `index.html` to update your information:
-   **Experience**: Update the `<ul>` list in the `.experience-box`.
-   **Certifications**: Edit content in the `.cert-box`.
-   **Courses**: Modify the text in the `.courses-box`.

### Fonts
Open `style.css` and find the `Typography Options` section. You can uncomment the desired font family:

```css
/* Option 1: Modern & Clean (Default) */
font-family: 'Noto Sans TC', sans-serif;

/* Option 2: Elegant & Formal */
/* font-family: 'Noto Serif TC', serif; */
```

### Images
-   **Profile Photo**: Replace `ann_trx.png` with your photo.
-   **Header Icon**: Replace `icon.png` with your preferred logo or icon.

## 📦 Deployment

This project is ready for deployment on platforms like Vercel or Netlify.

**Vercel (Recommended):**
1.  Push your changes to GitHub.
2.  Import the repository in Vercel.
3.  Deploy!

See [deploy.md](./deploy.md) for detailed instructions.

## 📄 PDF Export

You can generate a high-quality PDF version of the CV using the included Python script.

### Prerequisites
-   Python 3.x
-   Playwright

### Installation
1.  Install the required package:
    ```bash
    pip install playwright
    ```
2.  Install the Playwright browser binaries:
    ```bash
    playwright install chromium
    ```

### Usage
Run the script to generate the PDF:
```bash
python export_cv.py
```
This will create `index.pdf` in the same directory. You can also specify a different input file:
```bash
python export_cv.py my_cv.html
```

## 📄 License

This project is open source and available for personal use.
