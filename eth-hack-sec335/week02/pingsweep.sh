#!/bin/bash

for i in $(seq 2 50)
do
  ping_res=$(ping -c 1 10.0.5.$i)
  if [[ ! $ping_res =~ "100% packet loss" ]]; then
    echo ; echo -e "10.0.5.$i FOUND" ; echo 10.0.5.$i >> sweeper.txt
  else
    echo -e "10.0.5.$i not found";
  fi
done
