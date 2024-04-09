#!/bin/bash

## cut command
## -d for delimiter which will be ,
##  select the nth element with -f 3


echo "enter your text to split"
read text1

## cut -d , -f 4 <<< "Website, Domain, DNS, SMTP, 404"

myVar=$(cut -d , -f 3 <<< $text1)

echo "the answer is: $myVar"

#######################

myVar2=`cut -d , -f 2 <<< $text1`
echo "the second answer is: $myVar2"

#################################

now=$(date)

echo "today is $now"

#################################

my_var=$(ls \
-l)

echo "$my_var"

################################

## using the backslash for multi-line format

grep_awk_var=$(ls \
-l | grep other_if \
| awk '{ print $5 }'
)

echo "the value is: $grep_awk_var"





