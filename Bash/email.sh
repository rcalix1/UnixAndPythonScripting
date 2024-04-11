#!/bin/bash

## >> sudo apt-get install mailutils
## >> mail

Recipient="root"   ##"rcalix@pnw.edu"    ## to PNW should also work!
Mysubject="error installation"
Mymessage="Hello. I am getting an error with cuda6"
`mail -s $Mysubject $Recipient <<< $Mymessage`
