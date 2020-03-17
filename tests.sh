#!/bin/sh
set -e

SOURCE_DIR="pyskeleton"
TEST_DIR="tests"

if [ ! "$(command -v black)" ] || [ ! "$(command -v flake8)" ] || [ ! "$(command -v shellcheck)" ] || [ ! "$(command -v yamllint)" ]; then
  ./install.sh
fi

echo "Checking code style with black..."
black --check "$SOURCE_DIR" "$TEST_DIR"

echo "Linting with flake8..."
flake8 "$SOURCE_DIR" "$TEST_DIR"

echo "Linting Shell scripts with shellcheck"
# shellcheck disable=SC2046
shellcheck ./*.sh $(find "$SOURCE_DIR" "$TEST_DIR" -iname "*.sh")

echo "Linting YAML files with yamllint"
# shellcheck disable=SC2046
yamllint ./.*.y*ml ./*.y*ml $(find "$SOURCE_DIR" "$TEST_DIR" -iname "*.y*ml")
