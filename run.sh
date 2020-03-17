#!/bin/sh
set -e

if [ ! "$(command -v pyskeleton)" ]; then
  ./install.sh
fi

# shellcheck disable=SC2068
pyskeleton $@
