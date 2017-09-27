#!/bin/bash

#7.piemers
#skaitliska_vertiba='expr 2 + 2'
#echo "Summas vertiba: "$skaitliska_vertiba
#echo "Summas vertiba: $skaitliska_vertiba"

skaitliska_vertiba=`expr 2 + 2`
echo "Summas vertiba: "$skaitliska_vertiba
echo "Summas vertiba: $skaitliska_vertiba"

#skaitliska_vertiba=expr 2 + 2
#echo "Summas vertiba: "$skaitliska_vertiba
#echo "Summas vertiba: $skaitliska_vertiba"


#6.piemers
#echo $*
#echo "---------------"
#kartas_numurs=1
#for arguments in $*
#do 
#    echo $kartas_numurs". arguments - " $arguments
#    kartas_numurs=$kartas_numurs+1
#done

#5.piemers
#echo "Skriptam nodotu argumentu skaits:" $#
#echo "Argumentu saraksts (attelosana/ grupesana veids 1): " $*
#echo "Argumentu saraksts (attelosana/ grupesana veids 2): " $@
#echo "Pirma argumenta vertiba: " $1
#echo "Otra argumenta vertiba: " $2
#echo $1$2

#4.piemers
#echo "Izpildama skripta faila nosaukums: " $0
##echo $n
#echo "Skriptam nodotu argumentu skaits:" $#
#echo "Argumentu saraksts (attelosana/ grupesana veids 1): " $*
#echo "Argumentu saraksts (attelosana/ grupesana veids 2): " $@
##ech "Argumentu saraksts (attelosana/ grupesana veids 2): " $@
#echo "Iepreksejas komandas izpildes rezultats: " $?
#echo "Skripta izpildei pieskirtais procesa  numurs: " $$
##echo $!

#3. piemers
#N="Vards"
#echo $N
#unset N
#echo $N

#2.piemers
#N="Vards"
#readonly N
#echo $N
#N="Vards Uzvards"
#echo $N

#1.piemers
#N="Vards"
#echo $N

#0. piemers
#history > history_20170927.txt

