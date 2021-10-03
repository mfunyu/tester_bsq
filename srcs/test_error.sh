#!/bin/bash

source ./srcs/const.sh
source ./srcs/print_result.sh

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

read_error_map_check_log