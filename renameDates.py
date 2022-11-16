#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY

import shutil, os, re

datePattern = re.compile(r"""^(.*?)  # all text before the date
                         ((0|1)?\d)-      # one or two digits for month
                         ((0|1|2|3)?\d)-  # one or two digits for the day
                         ((19|20)\d\d)    # four digits for the year
                         (.*?)$           # all remaining text
                         """, re.VERBOSE)

# loop over files in the directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    
    # skip files w/o date
    if mo == None:
        continue
    
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    datePart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    
    euroFilename = beforePart + datePart + '-' + monthPart + '-' + yearPart + afterPart
    
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    
    # rename the files
    print(f'Renaming "{amerFilename}" to "{euroFilename}"')
    shutil.move(amerFilename, euroFilename)