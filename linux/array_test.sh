#!bin/bash
arr=(a b c) # enclosed in the bracket
echo ${arr[*]}
for i in ${arr[@]}
do
	echo $i
done

#string to array
s="a b c d e f g"
arr_s=($s)
# echo ${arr_s[@]}
# for i in ${arr_s[@]}
# do
# 	echo $i
# done
echo "${#arr[@]}"
echo "for 1-5"
for i in `seq ${#arr_s[@]}`
do
	echo ${arr_s[i-1]}
done
echo $(seq 0 5)