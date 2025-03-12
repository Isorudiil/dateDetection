import re
import datetime

# Plan:
# get user input for date
# check if user input is valid
# if user input is not valid, keep requesting user input until valid
# once user input is valid, print user input in one form or another


def dobValid():
    print('This birthday is valid')


def dobInvalid():
    print('\nThis birthday is invalid\n')
    dob = getInput()
    parseInput(dob)


# creates regular expression formatting
# searches user input for properly formatted regex
# returns for further use by program
def getInput():
    dateRegex = re.compile(r'([0-3][0-9])/([0-1][0-9])/([1-2]\d\d\d)')
    badDOB = True
    while badDOB:
        dob = dateRegex.search(input('Please enter your DOB (DD/MM/YYYY): '))
        if dob == None:
            print('\nDOB must be positive numbers and forward slashes only!\nPlease following formatting guide: DD/MM/YYYY\n')
        else:
            return dob


def parseInput(dob):
    m = int(dob.group(2))
    d = int(dob.group(1))
    y = int(dob.group(3))


    if d == 31:
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            dobValid()
    if 0 < d <= 30:
        if m == 2:
            if d == 29:
                if y % 4 == 0:
                    dobValid()
                else:
                    dobInvalid()
            if d <= 28:
                dobValid()
        elif 0 < m <= 12:
            dobValid()
        else:
            dobInvalid()
    else:
        dobInvalid()


if __name__ == '__main__':
    dob = getInput()
    parseInput(dob)
