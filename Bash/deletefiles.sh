#!/bin/bash

myfile='cats.txt'
## touch $myfile

## check if file exists
if [ -f $myfile ]; then
   ## rm planes.txt
   rm $myfile
   echo "$myfile has been deleted"
else
   echo "the file $myfile does not exist"
fi
