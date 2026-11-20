# The Kinziger Lab website

This repository is the website of the Kinziger Lab, Department of Fisheries Biology, Cal Poly Humboldt:
https://kinzigerlab.github.io

The site is one page, `index.html`, plus the photographs in `img/`. GitHub Pages serves both as they are.

## Updating the site

`index.html` is generated, so do not edit it by hand.

1. Edit `src/content.py`. All text, people, alumni and publications are there.
2. Put any new photograph in `img/`.
3. Run `python3 src/build.py --repo`. This rewrites `index.html`.
4. Commit and push. The site updates within a few minutes.

`src/style.css` holds the design. `src/site.js` is the small script behind the navigation and the publication
filter. Python 3 is enough; nothing needs installing.

## Visit counter

The site counts visits with GoatCounter. It sets no cookies and stores nothing about visitors. The numbers are at
https://kinzigerlab.goatcounter.com (sign-in required).

- `count.v5.js` is GoatCounter's own counter script, version 5, unchanged. It is kept here so the site loads no
  script from another server. Its fingerprint matches the one GoatCounter publishes for that version:
  `sha384-atnOLvQb9t+jTSipvd75X2yginT4PjVbqDdlJAmxMm+wYElFmeR6EmLP5bYeoRVQ`
- Each view is counted as its own page: `/`, `/research`, `/people`, `/publications`, `/join`. The code is under
  "visit counting" in `src/site.js`.
- The account name is `GOATCOUNTER`, at the end of `src/content.py`. Set it to `""` and rebuild to stop counting.
- To leave your own visits out, open https://kinzigerlab.github.io/#toggle-goatcounter once in each browser you use.
  Opening it again turns counting back on for that browser.
