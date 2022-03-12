#!/bin/bash
set -e -x
BACKEND=$1
EXPNAME=$2
XML_REPORT="sequential_test_results.xml"
export TEST_ARGS="-v -s -rsx --backend=${BACKEND} "

JENKINS_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/../"
export TEST_DATA_HOST="${TEST_DATA_HOST}/physics/"
if [ ${python_env} == "virtualenv" ]; then
    export TEST_DATA_RUN_LOC=${TEST_DATA_HOST}
    export TEST_ARGS="${TEST_ARGS} --junitxml=${JENKINS_DIR}/${XML_REPORT}"
    CONTAINER_CMD="srun" make physics_savepoint_tests
else
    export TEST_ARGS="${TEST_ARGS} --junitxml=/${XML_REPORT}"
    make physics_savepoint_tests
fi
