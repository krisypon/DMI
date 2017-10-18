#!/bin/bash

echo "Input x: "
read x
echo "Input y: "
read y
echo "Input z: "
read z

a = 0

for i in $x $y; do c=`expr $x + $y`
echo "Atbilde"$c; done

if (( $x !=  $y && $x != $z && $y != $z ))
then
	if (( $x > $a))
	then 
	$a = $x 
	elif (( $y > $a ))
	then
	echo "x<y<z"
	elif (( ))
fi
else
echo "x is equal y & z"
fi
