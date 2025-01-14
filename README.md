# phenotype_from_genotype
Repo for tracking my thesis' conversion to jupyter book.

## Setup:

0. Install Python, Install R

1. Clone git repo.

2. Use a virtual environment:
```bash

python3 -m venv venv/
source venv/bin/activate
```

3. Install requirements
```bash
pip3 install -r requirements.txt
pip3 install -r requirements-dev.txt
```

- Install IRkernel 
`Rscript install.R`

## Website:
To build html:
`jupyter-book build book`

For interactive images:
Replace the `img` tags with an `iframe` tag pointing to the standalone html (which must be copied into `_build/html/_images`). (Not ideal. Hopefully they will fix.). I.e. Copy in the following:
```html
<!--
<a class="reference internal image-reference" href="../_images/combining_funnel_interactive.html"><img alt="../_images/combining_funnel_interactive.html" src="../_images/combining_funnel_interactive.html" style="height: 150px;" /></a> -->
<iframe src="../_images/combining_funnel_interactive.html" width="600px" height="300px" style="border:none;"></iframe>
```

To view/check:
`open book/_build/html/index.html`

## To build PDF
<!--
`jupyter-book build book --builder pdfhtml`
`jupyter-book build book --builder pdflatex` <- fails
-->

<!--
First build latex:
`jupyter-book build book --builder latex`

Next edit `_build/latex/thesis.tex`:
- Delete the jupyter-book intro
- Delete the biography (auto-generated, so there will be two)
- Make sure anything don't want numbered has a * after it e.g. `\chapter*{Glossary}` 
- Delete everything to do with `\index`
- Interactive figures: add in the static versions
- Code blocks: remove/link to website.

Finally, move to the `latex` directory and run `make`.
-->

<!-- ` jupyter-book build . --builder pdfhtml` (This doesn't work if you have a venv at the moment)-->



`jupyter-book build book --builder pdfhtml --toc book/_toc.yml`
- add page numbers from page 11 to end using [https://www.ilovepdf.com/add_pdf_page_number](https://www.ilovepdf.com/add_pdf_page_number)
- remove first 2 pages in preview

<!-- Note when you make the PDF, it will break the website html (there will be a new pdf html version), so you must then rebuild the normal version `juputer-book build book` -->