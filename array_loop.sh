
#!/bin/bash

array=( "$@" )
#Cik argumenti atnaca mana riciba:
n=$#

#echo array   (nestrada)
#echo ${array[0]}
#echo ${array[1]}

#Kartas numurs
k=0 ##k=`expr $n - 1`
while (( $k < $n )) ##$k >= 0
do
	echo ${array[$k]} #$n - $k -1
	k=`expr $k + 1` ##k=`expr $k -1`
done
