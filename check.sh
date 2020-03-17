#!/bin/bash
set -e

SOURCE_DIR="pyskeleton"
TEST_DIR="tests"
MIN_COVERAGE=80



echo "Checking code style with black"
black --check "$SOURCE_DIR" "$TEST_DIR"
echo

echo "Linting with flake8"
flake8 "$SOURCE_DIR" "$TEST_DIR"
echo

echo "Linting Shell scripts with shellcheck"
# shellcheck disable=SC2046
shellcheck ./*.sh $(find "$SOURCE_DIR" "$TEST_DIR" -iname "*.sh")
echo

echo "Linting YAML files with yamllint"
# shellcheck disable=SC2046
yamllint .yamllint $(find ./ -iname "*.y*ml")
echo

echo "Running unit tests"
coverage run --source="$SOURCE_DIR" -m unittest
echo

echo "Generating coverage report, check at least $MIN_COVERAGE% of the code is covered by the tests"
coverage report --fail-under="$MIN_COVERAGE"
echo
