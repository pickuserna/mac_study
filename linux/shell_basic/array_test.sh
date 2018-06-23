#!/bin/bash

a=(1 2 3)
echo ${a[@]}
echo ${a[*]}
for i in ${a[*]}
do 
    echo $i
done
