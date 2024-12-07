#!/bin/bash

logDir="/var/log/apache2/"
allLogs=$(ls "${logDir}" | grep "access.log" | grep -v "other_vhosts")
echo "${allLogs}"

:> access.txt

for i in ${allLogs}
do
    cat "${logDir}${i}" >> access.txt
done


