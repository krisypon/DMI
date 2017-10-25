#!/bin/bash
echo "Ievadi skaitlu skaitu: "
read n

for (( i = 1; i <= n; i++))
do
  echo -n "Ievadi $i. skaitli: "
  read x
  sum=`expr $sum + $x`

    if (( i == 1 ))
    then
     min=$x
     min1=$x
     min2=$x
    else
	if (( $min > $x ))
	then
	min=$x
	fi
fi
    	if (( $min1 > $x && $x > $min))
	then
	min1=$x
	fi

	if (( $min2 > $x && $x > $min1))
	then
	min2=$x
	fi

done
echo " "
echo $min
echo $min1
echo $min2
echo $sum

