# CV Deployment Guide

Since this project is hosted on GitHub, the easiest way to deploy is using Vercel's GitHub integration.

## Method: Vercel + GitHub (Recommended)

1.  **Log in to Vercel**:
    Go to [vercel.com](https://vercel.com) and log in.

2.  **Import Project**:
    -   Click the **"Add New..."** button and select **"Project"**.
    -   Select **"Continue with GitHub"** if asked.
    -   Find the repository **`figuedmundo/ann-cv`** in the list and click **"Import"**.

3.  **Configure & Deploy**:
    -   **Project Name**: You can leave it as `ann-cv` or change it.
    -   **Framework Preset**: Select "Other" (since this is plain HTML/CSS).
    -   **Root Directory**: Leave as `./`.
    -   Click **"Deploy"**.

4.  **Done!**
    Vercel will build your site and give you a live URL (e.g., `ann-cv.vercel.app`).

## Continuous Deployment
Because you linked the repository, every time you push changes to the `main` branch on GitHub:
```bash
git add .
git commit -m "Update CV"
git push
```
Vercel will **automatically** redeploy your site with the new changes.

## Alternative: Vercel CLI
If you prefer not to use the dashboard:
1.  Run `npx vercel` in this folder.
2.  Follow the prompts to link and deploy.
