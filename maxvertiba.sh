#!/bin/bash

echo "Input x: "
read x
echo "Input y: "
read y
echo "Input z: "
read z

#if (( $x > $y && $x > $z ))
#then
#big=$x
#elif (( $y > $x && $y > $z ))
#then
#big=$y
#else
#big=$z
#fi
#echo "The biggest: "$big


if (( $x < $y))
then
	max=$y
	if (( $z > $max ))
	then
	max=$z
	fi
else
        max=$x
	if (( $z > $max ))
	then
	max=$z
	fi
fi
echo "The biggest: "$max
