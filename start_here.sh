#!/bin/bash
sudo pkill -9 python3
export BITLYTOKEN=
export JWTUSER=test 
export JWTPASS=test
export JWT_SECRET_KEY=changethis
source env/bin/activate
python3 app.py
