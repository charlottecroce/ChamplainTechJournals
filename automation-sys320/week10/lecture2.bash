#!/bin/bash

function countingCurlAccess(){
    file="/var/log/apache2/access.log"
    curlCounts=$(cat "$file" | cut -d' ' -f1,12 | grep "curl" | uniq -c)
}

countingCurlAccess
echo "$curlCounts"
