import pyinputplus as pyip
import sys, time

print('Welcome to my sandwich shop! these are our prices.')

# Prints a pricelist that is alligned with rjust and ljust per the users input
pricelist = {'bread': '50', 'protein': '25', 'cheese': '20', 'mayo': '10', 'mustard': '10', 'lettuce': '5', 'tomato': '5'}
def printPricelist(itemsDict, leftWidth, rightWidth):
    print('PRICELIST'.center(leftWidth + rightWidth, '-'))
    for k, v in pricelist.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
printPricelist(pricelist, 12, 5)

response = pyip.inputYesNo('Would you like to order a sandwich?\n')
if response == 'no':
    sys.exit('Have a nice day!')

breadType = pyip.inputMenu(['wheat', 'white', 'sourdough'], numbered=True)
proteinType = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
cheese = pyip.inputYesNo('Would you like cheese on your sandwich?\n')
if cheese == 'yes':
    cheeseType = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], numbered=True)

listAdd = ['mayo', 'mustard', 'lettuce', 'tomato']
for i in listAdd:
    toppings = pyip.inputYesNo('Would you like ' + i + ' on your sandwich?\n')

amountOfSandwiches = pyip.inputInt('How many sandwiches would you like?\n', min=1)

print("Thank you for your order! just a moment while we prepare your order, please.")
time.sleep(3)
print('here you go, enjoy your sandwich!')
