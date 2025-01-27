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
* 
  


