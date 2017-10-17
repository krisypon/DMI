#!/bin/bash

echo -n "Ievadi x: "
read x

echo -n "Ievadi y: "
read y

#sum=`expr $x + $y`
#echo "x+y="$sum
#st=`expr $x - $y`
#echo "x-y="$st
#reiz=`expr $x \* $y`
#echo "x*y="$reiz

if [ $x -gt $y ]
then
echo "x lielaks par y"
else 
#if
#[ $x -lt $y ]
#then
echo "y lielaks par x"
#else
#echo "x vienads ar y"
fi

if [ $x == $y ]
then
echo "x is equal to y"
fi

if [ $x != $y ]
then
echo "x is not equal to y"
fi
