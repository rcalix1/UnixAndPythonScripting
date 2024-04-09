#!/bin/bash

base="w"
dm="wx"
if [ "$base" = "Z" ] && [ "$dm" = "X" ]; then
        echo 'A'
elif [ "$base" = "w" ] && [ "$dm" = "wx" ]; then
        echo 'B'
else
        echo 'RC'
fi
