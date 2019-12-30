spam = []

def sepList(myList):

    try:
        for i in myList[0:-2]:
            print(i, end=', ')
        print(myList[-2] + ' and ', end='')
        print(myList[-1])

    except IndexError:
        print('That list is empty')

sepList(spam)