#!/bin/bash

echo "Input x: "
read x
echo "Input y: "
read y

for i in $x $y; do c=`expr $x + $y`
echo "Atbilde"$c; done


if (( $x > $y ))
then
echo "x > y"
elif (( $x < $y ))
then 
echo "x < y"
fi

if (( $x !=  $y ))
then
	if (( $x > $y ))
	then 
	echo "x>y"
	else
	echo "x<y"
	fi
else
echo "x is equal y"
fi
