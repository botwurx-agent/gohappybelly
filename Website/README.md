# Go Happy Belly Website

The Go Happy Belly homepage, kept here in version control as a self-contained copy.

## Files
- `index.html` — the homepage (copy of the original `Documents/Funnel Assets/gohappybelly-homepage.html`, renamed to the standard web entry-point name).
- `IMG_8247.jpg`, `Alina_Fence.jpg` — the local images the page references. They sit next to `index.html` so the page renders as a self-contained folder.

## To preview locally
Open `index.html` in a browser, or from this folder run a simple static server (for example `python3 -m http.server`) and visit the printed address.

## Known dependencies and gaps
- **Remote logo:** the page loads the Go Happy Belly logo from Mailchimp's CDN (`mcusercontent.com/...`), so it needs an internet connection to show that image. This is the same logo URL used across the email templates.
- **Missing favicon:** `index.html` references `favicon.png`, which is not currently in the project. The page still works; the browser tab icon just falls back to a default. Drop a `favicon.png` into this folder to fix it.

## Notes
- This is a copy for versioning and reference. The canonical original still lives at `Documents/Funnel Assets/gohappybelly-homepage.html`. If you want a single source of truth going forward, tell me and I will consolidate to just this folder.
- A larger raw photo library (source photos, not all used by this page) lives outside the repo at `~/Documents/GoHappyBelly/Website Images/`. It was left out to keep the repo lean; ask if you want specific images or the whole set brought in.
