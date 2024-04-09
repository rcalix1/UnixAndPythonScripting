#!/bin/bash

## getting the avg ping time

_ping="/bin/ping"
domain="8.8.8.8"


all_ping_vals=$(${_ping} \
-c 4 \
${domain} | grep rtt | awk '{print $4}' )

echo "$all_ping_vals"


other_res=$(echo "$all_ping_vals" | cut -d / -f 2 )
echo "$other_res"


ping_avg=$(${_ping} \
-c 4 \
${domain} | grep rtt | awk '{print $4}' | cut -d / -f 3 )

echo "$ping_avg"
