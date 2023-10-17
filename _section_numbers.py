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
html_files.remove('docs/00-index.html')
html_files.sort()

# set counter
cnt = 0

# loop html files
for htmlf in html_files:

    # initialise template
    with open(htmlf) as file :
      html_content = file.read()

    # update TOC
    html_content = html_content.replace('<span class="header-section-number">1', \
                                        '<span class="header-section-number">' + str(1 + cnt))
    # update counter
    cnt += 1
    
    # write
    with open(htmlf, 'w') as file:
        file.write(html_content)
