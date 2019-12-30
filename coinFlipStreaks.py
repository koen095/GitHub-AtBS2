import random
numberOfStreaks = 0
for experimentNumber in range(10000):

    # Code that creates a list of 100 'heads' or 'tails' values.
    experiment = []

    def flip():

        coinFlip = random.randint(0,1)

        if coinFlip == 0:
            experiment.append('H')
        elif coinFlip == 1:
            experiment.append('T')

    for i in range(0, 100):
        flip()

    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))