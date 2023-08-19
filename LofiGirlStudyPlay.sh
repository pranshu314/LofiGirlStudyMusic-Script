#!/bin/bash

url=`python3 ~/.scripts/LofiGirlStudy/LofiGirlStudyUrl.py`
# echo $url
exec mpv --no-terminal --no-video "$url" 2>/dev/null

