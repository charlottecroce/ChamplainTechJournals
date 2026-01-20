#!/bin/sh
fping -g 10.0.5.2 10.0.5.50 > sweep2.txt; ; sed -i '/unreachable/d' sweep2.txt
