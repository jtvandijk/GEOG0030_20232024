# libraries
# conda env: html
import pandas as pd
import os
import glob

# placeholder
html_files = []

# get html files
files = glob.glob('docs/*')
for f in files:
    if os.path.basename(f).endswith('.html'):
        html_files.append(f)

# only keep chapters
html_files.remove('docs/index.html')
html_files.sort()

# set counter
cnt = 0

# loop html files: fix headers, fix individual TOC entries
for htmlf in html_files:

    # initialise template
    with open(htmlf) as file:
      html_content = file.read()

    # update headers
    html_content = html_content.replace('<span class="header-section-number">1', \
                                        '<span class="header-section-number">' + str(0 + cnt))

    # update counter
    cnt += 1
    
    # update TOC chapter 1
    html_content = html_content.replace('<span class="menu-text">Geocomputation: An Introduction</span>', \
                                        '<span class="menu-text">1 Geocomputation: An Introduction</span>')
    # update TOC chapter 2
    html_content = html_content.replace('<span class="menu-text">GIScience and GIS software</span>', \
                                        '<span class="menu-text">2 GIScience and GIS software</span>')
    
    # update TOC chapter 11
    html_content = html_content.replace('<span class="menu-text">Data Sources</span>', \
                                        '<span class="menu-text">11 Data Sources</span>')

    # write
    with open(htmlf, 'w') as file:
        file.write(html_content)

# fix index page redirect
htmlredir = 'docs/index.html'
with open(htmlredir) as file:
    html_content = file.read()

    # update redirect
    html_content = html_content.replace('01-introduction.html', \
                                          '00-index.html')

    # write
    with open (htmlredir, 'w') as file:
      file.write(html_content)