#!/bin/bash

num=("$@")
n=$#

sortednum=($(printf "%s\n" "${num[@]}" | sort -n))
echo ${sortednum[@]}
echo "MIN:" ${sortednum[0]}
echo "MAX:" ${sortednum[n-1]}

#Mediana
if (( n%2 != 0 ))
then
	echo -n "Median:"
	echo "${sortednum[($n-1)/2]}" | bc
else
	echo -n "Median:"
	echo "scale=1;(${sortednum[$n/2]} + ${sortednum[$n/2-1]})/2" |bc
fi

#Moda
t=0
a1=${sortednum[$t]}	#skaitlis
a2=1			#cik reizes atkartojas
b1=$a1			#skaitlis
b2=$a2			#cik reizes atkartojas

while (( $t < $n ))
do
	t=`expr $t + 1`
	if [[ "$a1" == "${sortednum[t]}" ]]
	then
		a2=`expr $a2 + 1`
	else
		a1=${sortednum[$t]}
		a2=1
	fi

	if (( $a2 > $b2))
	then
		b1=$a1
		b2=$a2
	fi
done

if (( $b2 == 1 ))
then
	echo "Visi skaitli atkartojas vienu reizi"
else
	echo "Moda:" $b1
fi
