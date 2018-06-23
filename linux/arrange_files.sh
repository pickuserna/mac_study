#!/bin/bash

# walk files under folder and arrange them by the suffix
folder="$HOME/Downloads"
# array ${} # ${!a[@]}, ${a[@]}
folders=("$folder/video" "$folder/docs")
types[0]="mp4 rmvb mkv"
types[1]="pages pdf doc txt"
# cd

for idx in ${!types[@]}
do
	echo $idx, ${types[idx]}
	for each_type in ${types[idx]}
	do
		dest_folder=${folders[$idx]}
		if [ ! -d $dest_folder ];	
		then
			echo makedir $dest_folder
			mkdir -p $dest_folder
		fi
		# silence, not overwrite
		find $folder -name "*.$each_type" -exec mv -n {} $dest_folder 2>/dev/null \; 
	done
done

