#!/bin/sh

a=10
b=20

# 1.piemers - izteiksmes pieraksts
val11="expr 2+2"
echo "2 + 2 rezultats (pedinas, nav atstarpes) "$val11
val12="expr 2 + 2"
echo "2 + 2 rezultats (pedinas, ir atstarpes) "$val12
val13='expr 2+2'
echo "2 + 2 rezultats (parastie apostrofi, nav atstarpes) "$val13
val14='expr 2 + 2'
echo "2 + 2 rezultats (parastie apostrofi, ir atstarpes) "$val14
val15=`expr 2+2`
echo "2 + 2 rezultats (neparastie apostrofi, nav atstarpes) "$val15
val16='expr 2 + 2'
echo "2 + 2 rezultats (neparastie apostrofi, ir atstarpes) "$val16

#val=`expr 2 + 2`
#echo "Total value : $val"

#val=`expr $a + $b`
#echo "Total value : $val"

#val=`expr $a - $b`
#echo "Total value : $val"

#val=`expr $a \* $b2`
#echo "Total value : $val"

