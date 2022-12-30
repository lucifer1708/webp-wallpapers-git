#!/bin/bash


ls images/ | grep -v .webp | grep .$1 | cut -d '.' -f1 | xargs -I {} convert images/{}.$1  -resize 1920 images/{}.webp;
