import pyinputplus as pyip

while True:
    response = pyip.inputYesNo('want to know how to keep an idiot busy?\n')
    if response == 'no':
        break
print('Thank you. Have a nice day')
