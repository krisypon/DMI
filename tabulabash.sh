#!/bin/bash

echo -n "Ievadi x: "
read x

echo "x = "$x
echo -e "x || \t%1 | \t%2 | \t%3 | \t%4 | \t%5 | \t%10"
echo "----------------------------------------------------"

k=1

while (( $k < 11 ))
do
a=`expr $x % 1`
b=`expr $x % 2`
c=`expr $x % 3`
d=`expr $x % 4`
e=`expr $x % 5`
f=`expr $x % 10`
k=`expr $k + 1`
echo -e "$x || \t$a  | \t$b  | \t$c  | \t$d  | \t$e  | \t$f"
x=`expr $x + 1`
done
