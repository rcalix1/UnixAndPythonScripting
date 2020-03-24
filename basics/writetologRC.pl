#!/usr/bin/perl

use strict;
use warnings;

use Sys::Syslog qw(:DEFAULT setlogsock); #library for syslog functions

setlogsock('unix');

openlog('writetologRC.pl', 'pid', 'user');
syslog('info', 'your name');
closelog();


