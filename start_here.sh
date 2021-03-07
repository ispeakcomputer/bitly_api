#!/bin/bash

export BITLYTOKEN=
source env/bin/activate
python3 app.py
trap 'pkill -9 python3' EXIT
