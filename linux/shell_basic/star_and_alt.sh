#!/bin/bash
echo "$* is ", "$*"
for i in "$*"
do 
	echo $i
done
echo "$@ is ", "$@"

for j in "$@"
do 
	echo $j
done
