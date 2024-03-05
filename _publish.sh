#! /bin/bash

# clear
# rm -r *_cache *_files

# render
quarto render

# fix section numbers
source activate simple
python _section_numbers.py

# track changes
git add .
git commit -m "$1"

# publish
git push
