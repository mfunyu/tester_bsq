#!/bin/bash

source ./srcs/const.sh
source ./srcs/print_result.sh

check_ans (){
	map=$( basename $1 .map)
	python3 ./srcs/test.py $map
}

read_correct_map_check_ans (){
	for map in $( ls ${MAPDIR}/ | grep -v error); do
		printf "${PROMPT}${BSQ} ${MAPDIR}/${map}${RESET} "
		$BSQ ${MAPDIR}/$map > tmp
		ret=$?
		if [ $ret != 0 ]; then
			print_result $ret
		else
			check_ans $map
			print_result $?
		fi
	done
}

read_correct_map_check_ans