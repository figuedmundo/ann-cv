import os
import sys
from playwright.sync_api import sync_playwright

def generate_pdf(input_path, output_path):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # Convert file path to file:// URL
        file_url = f"file://{os.path.abspath(input_path)}"
        print(f"Opening: {file_url}")
        
        page.goto(file_url)
        
        # Wait for fonts and content
        page.wait_for_load_state('networkidle')
        
        # A4 measurements in CSS pixels (approx 96 DPI)
        # However, page.pdf uses strict dimensions.
        print("Generating PDF...")
        page.pdf(
            path=output_path,
            format="A4",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"}
        )
        
        print(f"PDF saved to: {output_path}")
        browser.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python export_cv.py <input_html_file>")
        # Default to index.html in the same directory
        input_file = "index.html"
    else:
        input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"Error: File {input_file} not found.")
        sys.exit(1)
        
    output_file = os.path.splitext(input_file)[0] + ".pdf"
    generate_pdf(input_file, output_file)
