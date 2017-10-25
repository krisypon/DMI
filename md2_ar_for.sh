#!/bin/bash
#No ievaditiem skaitliem parada min un max
min=0
max=0
vid=0
echo "Ievadi skaitlu skaitu: "
read n 

for (( i = 1; i <= n; i++))
do
echo -n "Ievadi $i. skaitli: "
read x
sum=`expr $sum + $x`
#max un min
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
#moda
#if (( i == 1))
#then 
#m=$x
#else

if (( n == 3 ))
then
echo $min `expr $sum - $min - $max` $max
fi

echo "Statistika:"
echo "Min: "$min
echo "Max: "$max
#echo "Vid.arifmetiskais: " $(bc <<< `expr $sum / $n `)
echo $sum / $n |bc
