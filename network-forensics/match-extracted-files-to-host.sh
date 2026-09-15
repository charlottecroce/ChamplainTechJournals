#!/bin/bash

for file in extract_files/*; do
    fuid=$(basename "$file")
    echo "--- $fuid ---"
    grep -F "$fuid" files.log
    echo
done
