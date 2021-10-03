#!/bin/bash

source ./srcs/print_result.sh

BSQ=../bsq
MAPDIR=./maps

ERR_MSG="map error"


# define
THICK="\033[1m"
CYAN="\033[1;36m"
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
RESET="\033[m"
PROMPT="${CYAN}$>${RESET}"

# from cmd line
	# error map
	# normal map
# from std input
	# normal map (generate now)
	# error map (read from file)


check_ans (){
	map=$( basename $1 .map)
	python3 ./srcs/test.py $map
}

read_correct_map_check_ans (){
	for map in $( ls ${MAPDIR}/ | grep -v error); do
		printf "${PROMPT}${BSQ} ${MAPDIR}/${map}${RESET}\n"
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

read_error_map_check_log (){
	for map in $( ls ${MAPDIR}/ | grep error); do
		printf "${PROMPT}${BSQ} ${MAPDIR}/${map}${RESET}\n"
		$BSQ ${MAPDIR}/$map 2> error_log 1> /dev/null
		ret=$?
		if [ $ret != 0 ]; then
			print_result $ret
		else
			cat error_log
			diff error_log <(echo $ERR_MSG) > /dev/null
			print_result $?
		fi
	done
}

read_correct_map_check_ans
read_error_map_check_log