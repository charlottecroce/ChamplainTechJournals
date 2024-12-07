#!/bin/bash

file="/var/log/apache2/access.log"

results=$(cat $file | cut -d' ' -f1,7 | tr -d "[")

function pageCount(){
    counts=$(awk '{print $7}' $file | sort | uniq -c)
}

pageCount
echo "$counts"

#echo "$results"
