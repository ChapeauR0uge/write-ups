#!/bin/bash

if [ $# != "1" ]
then
    echo -e "filename not found!"
    echo -e "usage: $0 <filename>"
else
    python3 DNAdecoder.py $1
    cat flag.txt
    rm flag.txt
fi
