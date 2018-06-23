#!/bin/bash
# read the configuration files
FILE_NAME='arrange_config.conf'
BASE_ROOT="$HOME/Downloads"
# function read_from_file(){
# 	while read LINE
# 	do

# 	args=`echo $LINE | awk '{print $1 " " $2}'`
# 	# args=($args) # make it an array
# 	# types=$(get_type_array ${args[0]})
# 	echo $args
# 	#for t in $types
# 	#do
# 	#	cd $BASEROOT
# 	#	mv *.$t $BASEROOT/downloads 2>/dev/null
# 	#done
# 	done < $FILENAME
# }
# function get_type_array(){
# 	arr=`echo $1 | tr -d ":" | tr ";" " "`
# 	echo $arr
# }
# echo $@ # all the arguments
# cur_dir=`pwd`
# echo $cur_dir
function process(){
	cnt=0
	cat $FILE_NAME | while read line
	do
		let cnt+=1
		if [ $cnt = 1 ]
		then 
			echo "first loop, jump over !"
			continue
		fi
		columns=(`echo $line | xargs`)
		types=(`echo ${columns[0]} | tr ";" " "`)
		sub_dir=${columns[1]}
		total_dir=$BASE_ROOT/$sub_dir
		echo $total_dir

		if ! [ -d $total_dir ]
		then
			echo "make dir: ", $total_dir
			mkdir $total_dir
		fi
		echo ${types[@]}
		for t in ${types[@]}
		do
			echo $t
			find_lines_count=`find $BASE_ROOT -name "*.$t" | wc -l`
			echo $find_lines_count
			if [ $find_lines_count -eq 0 ]
			then
				continue
			else
				find $BASE_ROOT -name "*.$t" -exec mv "{}" $total_dir \; 2 > /dev/null
			fi
			echo "one loop finished"
		done
	done
}
process
