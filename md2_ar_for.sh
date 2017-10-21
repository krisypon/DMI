#!/bin/bash
#No ievaditiem skaitliem parada min un max
min=0
max=0
vid=0

for i in 1 2 3 
do
echo -n "Ievadi $i. skaitli: "
read x
vid=`expr $vid + $x`

if (( i == 1 ))
then
max=$x
min=$x
elif (( $min > $x ))
then
min=$x
elif (( $max < $x ))
then
max=$x
fi
done


echo "Min: "$min
echo "Vid: "`expr $vid - $min - $max`
echo "Max: "$max
