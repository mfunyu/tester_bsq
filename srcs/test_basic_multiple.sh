#!/bin/bash

source ./srcs/const.sh
source ./srcs/print_result.sh

check_ans (){
	maps_arg=""
	for map in "$@"; do
		map=$( basename $map .map)
		maps_arg="$maps_arg $map"
	done
	python3 ./srcs/test.py $maps_arg
}

read_multiple_maps_check_ans (){
	maps=""
	for map in $( ls ${MAPDIR}/ | grep -v error); do
		maps="${maps} ${MAPDIR}/${map}"
		printf "${PROMPT}${BSQ} ${maps}${RESET} "
		$BSQ $maps > tmp
		ret=$?
		if [ $ret != 0 ]; then
			print_result $ret
		else
			check_ans $maps
			print_result 0
		fi
	done
}

read_multiple_maps_check_ans