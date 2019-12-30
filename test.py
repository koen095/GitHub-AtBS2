pricelist = {'bread': '50', 'protein': '25', 'cheese': '20', 'mayo': '10', 'mustard': '10', 'lettuce': '5', 'tomato': '5'}
# Prints a pricelist that is alligned per the users input
def printPricelist(itemsDict, leftWidth, rightWidth):
    print('PRICELIST'.center(leftWidth + rightWidth, '-'))
    for k, v in pricelist.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
printPricelist(pricelist, 12, 5)
