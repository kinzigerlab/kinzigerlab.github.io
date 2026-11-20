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
