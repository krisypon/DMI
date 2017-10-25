#!/bin/bash

#if () then ... elif () then ... else ... fi
a=$1
if (( $a > 0 ))
then
	echo "Izdruka no galvena zara (ja gadijums) - $a > 0"
elif (( $a == 0 ))
then
	echo "Izdruka no alter  zara (ja gadijums) - $a == 0"
else 
	echo "Izdruka no galvena zara (ne gadijums) - $a > 0"
fi
echo " "
#if () then ... else ... fi
a=$1
if (( $a > 0 ))
then
	echo "Izdruka no galvena zara (ja gadijums) - $a > 0"
else
	echo "Izdruka no galvena zara (ne gadijums) - $a < 0"
fi
echo " "
#if () then ... fi
a=$1
if (( $a > 0 ))
then
	echo "Izdruka no galvena zara (ja gadijums) - $a > 0"
fi

