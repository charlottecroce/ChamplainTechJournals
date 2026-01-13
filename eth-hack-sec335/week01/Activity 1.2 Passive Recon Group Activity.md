# Activity 1.2 Passive Recon Group Activity

## theHarvester
```
theHarvester -d <yourorganization> -b all
```

## Netcraft
go to https://sitereport.netcraft.com/ to find public information on domains


## Metagoofil
Metagoofil is a tool developed by Christian Martorella. It features the ability to search and
extract metadata from local files or files located in a web page. This metadata can give us, the
pentester, an insight to the persons, names and emails leaked to these public documents, that
can be valuable for social engineering attacks. Unfortunately, metagoofil does not download files for us anymore. It does not work well.
In fact, it is removed from the Kali. However, we can work around this issue.

```
apt-get update
mkdir metagoofil
cd metagoofil
sudo git clone https://github.com/opsdisk/metagoofil.git
cd metagoofil
```
to view help
```
sudo python3 metagoofil.py -h
```
If you are getting errors about python’s googlesearch packet. You can fix that with
```
pip3 install google==2.0.1 --break-system-packages
```
make a directory to store files
```
mkdir metagoo_out
```
Then run a command like the following (but change to a domain you are testing):
```
sudo python3 metagoofil.py -d champlain.edu -t pdf -l 10
-f metagoo_out/mydomainfiles.txt
```

```download.bash
#! /bin/bash
input = “/home/champuser/metagoofil/metagoofil/metagoo_out/mydomainfiles.txt”
counter=0
while read -r line
do
curl “${line}” -o “/home/champuser/metagoofil/metagoofil/${counter}.pdf”
let counter++
done < “${input}”
```
