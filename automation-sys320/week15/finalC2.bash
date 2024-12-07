#!/bin/bash

cat access.log | cut -d' ' -f1,4,7 | tr -d '[' | \
egrep -i -f IOC.txt > report.txt
