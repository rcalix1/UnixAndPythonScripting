# System Administration with Unix/Linux And Python Scripting

* Examples of how to use Unix and Linux

## System Administration with Unix (Brief history)

* In 1955, the first IBM 704 becomes available
* Computers were expensive and needed to be shared for multiple users
* Time sharing (1961-1962): At MIT, Marjorie Merwin-Daggett, Robert C. Daley, and Fernando Corbato started thinking about the problem of having multiple users logged in. They published a paper on the topic (https://dl.acm.org/doi/10.1145/1460833.1460871).
* In 1964, MIT, GE, and Bell Labs started building a computer for time sharing (project Multics).
* 5 years later the project was still not resolved and Bell Labs pulled out of the project
* UNIX (1969-1973)
* Three engineers from Bell Labs who had worked on project multics decided to re-think and try it on their own. They were: Ken Thompson, Rudd Canaday, and Dennis Ritchie.
* Ken Thompson continued to work on it using their GE-645 computer.
* In the summer on 1969, Ken Thompson re-wrote the code for the OS, the shell, the editor, and the assembler. The goal was to make it look more like an OS.
* In 1970 the original UNIX (or UNICS) had ideas from Multics but was only for single use (no time sharing).
* By 1971, UNIX had incorporated commands like: cat, as (assembler), chdir, chmod, chown, cmp (compare 2 files), cp, date, dc (desk calculator), du (disk usage).
* By 1973, the idea of "pipe" had been introduced. Also, the "C" language had been invented at Bell Labs.
* The "pipe" was on of the first powerful use cases of UNIX.
* In 1973, Ken and Dennis submitted their paper at the ACM symposyum in the IBM auditorium. Their presentation was a success and people started to want UNIX.
* Because of legal contracts with the government, AT&T and Bell Labs could not sell UNIX. And people could get it under license.
* People at universities started modifying it and adding capabilities.
* Around 1980, TCP/IP sockets were added.
* By 1985, science calculations were now being performed and email was used on university campuses. 
* The rise of a new profession "System Admin" was also deing defined.
* Sys Admin professions start at universities supporting UNIX by students
* Evi Nemeth became known as "the mother of system administration". She hired many students to work as sys admins supporting the college of engineering at the University of Colorado.
* Their job: keep unix and the IT operation running, and improve it.
* By 1990, UNIX was a server solution. A solution for PC was needed.
* At this time, a new PC version of UNIX was presented called BSD. Everything looked promising.
* Unfortunately, in 1992, AT&T filed a lawsuit saying that UNIX belonged to them and that companies were copying their code.
* By 1995 the case was settled. Out 18,000 files of UNIX, 3 were found to be original source code. They were removed.
* UNIX could continue freely. Unfortunately, during this period of uncertainty, many switched to Windows.
* During this time, an undergrad student at Helsinki University named Linus Torvalds had been writing his own UNIX clone.
* By 1994, several versions of Linux were available.
* Microsft first released Windows NT in 1993.
* Becasue of the AT&T lawsuit, many companies adopted Windows for "time sharing" during the 1990's.
* By 2000, Linux/UNIX was not doing great.
* Once the internet and e-commerce took off, the advantages of Linux/Unix was clear. Many web servers ran apache and linux and we cheaper.
* Today, Linux is doing well. Mac OS X, for example, is based on UNIX.
* 
  
## The UNIX way

* Files are central to UNIX
* Everything in Linux is a File
* File System (Directory of files)
* Root of the File System is "/"
* Security: a) file ownership and b) access control
* Ownership -> In Linux, files have 2 owners which 1) user and 2) group
* For example:
* -rwxrwxr-x 1 seed physics  59 Jan 15 14:40 HelloWorld.py
* Example:
* Smith is in the "Chem" group
* smith needs access to file in the "physics" group
* how do you give her access?
* Options:
* a) make copies of the files
* b) make the file word readable
* c) make smith a member of the physics group (this one)

## Access Control

* chown and chgrp
* "File Modes" -> file protection flags
* We have 3 tyopes of access: 1) r -> read, 2) w -> write, and 3) x -> execute
* Special case: 4) s -> SETUID
* Access classes: 1) user (u), 2) group (g), other (o)
* $ chmod u+w file1.txt

## Quiz
* Using numeric access modes convert from this:
* -rwxr--rw- 1 dummy2 seed 0 Jan 27 13:48 test1.txt
* to
* -rwxrwxrwx 1 dummy2 seed 0 Jan 27 13:48 test1.txt
* Your answer should look like this:
* $  chmod some_number test1.txt
  
## Cron
* Task Scheduling
* crontab
* Periodic program execution
* Use cases:
* back up files at night
* run scripts
* crontab -> stands for "cron table"
* cron files are stored in /var/
* crontab entries direct cron to run commands at regular intervals
* To start cron do:
* $ crontab -e
* select the editor such as"nano"
* 

## Cron Syntax

* the cron file uses "one-line" entries to run tasks
* And each one of these entries has the following format:
* Format:
* minutes hours day-of-month month weekday command
* where the command is anything you could write on the terminal
* the first 5 fields specify the times at which "cron" should execute the command
* Description of the fields:
* minutes -> minutes after the hour -> Range: 0-59
* hours -> hours of the day -> Range: 0-23 (0 = midnight)
* day-of-month - > numeric day within a month -> 1-31
* month -> month of the year -> 1-12
* weekday -> day of the week - > Range: 0-6 (0 = sunday)
* Example 1:
* 0,15,30,45 * * * * echo date
* --> displays date every 15 minutes
* An entry in any of these fields (e.g. minutes, hours, etc.) can be a single number,
* a pair of numbers separated by dash (i.e. range), a comma separated list of numbers,
* or an asterisk
* An asterisk (*) is a wild card that represents all valid values for that field
* In the crontab you can use "##" to comment out a line
* Example 2:
* Anomaly detection system
* collect data with netstat, tcpdump, and then look for string using python
* Example 3:
* 0,10,20,30,40,50 7-18 * * *  ./a.exe
* runs a.exe every 10 minutes from 7am to 6pm daily
* Example 4:
* 0 0 * * *  find / -name *.c
* runs the find command at midnight
* Example 5:
* 0 4 * * * sh a.sh
* runs a shell script every day at 4 am
* Example 6:
* 30 3 1 * * python backup.py
* Runs script at 3:30 am on the first day of each month
* Example 7:
* 30 2 * * 0,6  sh test.sh
* Runs the script at 2:30 am on sunday and saturday

## Output Handling

1) Redirecting
2) piping
3) discarding


## Redirecting to a file

* command 2>&1 > file.txt
* 2 ..... refers to the second file descriptor of a process. Which is "stderr"
* ">" ..... means redirection
* &1  .....refers to first file descriptor of a process. Which is "stdout"

## Discarding

* command 2>&1 > /dev/null

## Cron Examples

* Example 8
* 30 11 31 12 * /usr/bin/wall % Happy New Year!
* Runs the wall command at 11:30 am on december 31 wishing everyone a happy new year
* Example 9
* $ * * 1 1 1 sh test.sh
* Day of the week and day of the month are "Or"ed
* if both are filled in , the entry is run on that day of the month
* and on matching day of the week
* therefore, this entry would run January 1 and every monday
* Example 10
* 0 1 * * * /bin/sh /var/adm/daily.sh  2>&1  |  mail root
* run daily script every morning at 1 am
* Example 11
* 0 2 * * 1 /bin/sh /var/adm/weekly.sh 2>&1  |  mail seed
* run weekly script every monday at 2 am and send results to seed
* 











