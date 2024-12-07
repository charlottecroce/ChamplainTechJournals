#!/bin/bash
# turn report.txt into an html report

echo -e "<html>\n<head>\n\t<style>\n\t\ttd {border: 1px solid black;}\n\t</style>\n</head>\n<body>\n<h3>Access logs with IOC indicators:</h3>\n<table>" > report.html

cat report.txt | while read -r line; do
    echo -e "\t<tr>\n" >> report.html
    for element in $line; do
        echo -e "\t\t<td>$element</td>" >> report.html
    done
    echo -e "\t</tr>" >> report.html
done

echo -e "</table>\n</body>\n</html>" >> report.html

cp report.html /var/www/html/report.html
