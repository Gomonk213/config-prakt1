#!/bin/sh
cd "$(dirname "$0")" || exit 1
python src/main.py "$@"
