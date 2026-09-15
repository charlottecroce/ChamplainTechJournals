#!/bin/bash

for file in extracted_files/*; do
    fuid=$(basename "$file")
    echo "--- $fuid ---"
    grep -F "$fuid" files.log
    echo
done
