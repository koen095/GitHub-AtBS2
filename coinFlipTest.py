import random

numberOfStreaks = 0
newList = []

def flip():

    coinFlip = random.randint(0,1)

    if coinFlip == 0:
        newList.append('H')
    elif coinFlip == 1:
        newList.append('T')

for i in range(0, 100):
    flip()

print(newList)

for i in newList:
    if count == 6
        numberOfStreaks += 1
    print('Count of streaks is: ' + str(numberOfStreaks))


