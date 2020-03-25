import stat, sys, os, string, commands
#getting search patterns  and searching

try:
    pattern = raw_input("enter file pattern to search for: \n")
    commandString = "find " + pattern
    commandOutput = commands.getoutput(commandString)
    findResults = string.split(commandOutput, "\n")    
    ## print out permissions
    print "Files"
    print commandOutput
    print '*************************'
    for file in findResults:
        mode=stat.S_IMODE(os.lstat(file)[stat.ST_MODE]) ## research this command
        print "Permissions for file ", file
        for level in "USR","GRP","OTH":
            for perm in "R","W","X":
                print mode
                print stat               
                ## now print out the permissions for 
                ## the files that meet the search criteria 
                ## e.g. *.py 

except:
    print "error"

