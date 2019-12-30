import re

# write reg expression for date format dd/mm/yyyy
dateRegex = re.compile(r'''
    (\d\d)          # Day
    (\/)            # Separator
    (\d\d)          # Month
    (\/)            # Separator
    (\d{4})         # Year
    ''', re.VERBOSE)

mo = dateRegex.search('it is 31/12/1000 today')

# Store strings in variables named: Day, Month, Year

day = int(mo.group(1))
month = int(mo.group(3))
year = int(mo.group(5))

# Write code for detection of valid date

def checkValidity():
    if day > 31:
        print('day cant be above 31')
    elif month > 12:
       print('Month cant be higher than 12')
    elif year < 1000 or year > 2999:
       print('Year has to be between 1000 and 2999')
    else:
        print(mo.group())

checkValidity()
