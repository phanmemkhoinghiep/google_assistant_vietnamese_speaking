#!/bin/bash
#!/usr/bin/python3.7
#!/home/pi/.local/lib/python3.7/site-packages
STRING="Automatic launching Google Assistant..."
PYTHON="/usr/bin/python3.7"
BOT_ROOT="/home/pi/google_assistant_vietnamese_speaking/src"
BOT="pushtotalk.so"

pushd . > /dev/null 2>&1
cd $BOT_ROOT

echo $STRING
$PYTHON -m "$BOT"

popd > /dev/null 2>&1
