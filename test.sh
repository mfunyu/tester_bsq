#!/bin/bash

source ./srcs/const.sh

TESTS=$( ls ${SRCS_DIR} | grep "test_")

single_test (){
	printf "${CYAN}-------------$( basename ${1} .sh)--------------${RESET}\n"
	${SRCS_DIR}/${1}
	echo
}

all_bash_tests (){
	for test in ${TESTS}; do
		single_test $test
	done
}

print_help (){
	printf "${CYAN}Call test.sh with a cmd arg to exec single test\n${RESET}"
	for test in ${TESTS[@]}; do
		printf "$test: ./test.sh $( basename ${test:5:10} .sh)\n"
	done
}

if [ -e $1 ]; then
	all_bash_tests
elif [ "$1" == "help" ]; then
	print_help
elif [ "$1" ]; then
	single_test "test_${1}.sh"
fi