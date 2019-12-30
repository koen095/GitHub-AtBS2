
chessDict = {}

def isValidChessBoard(chessDict):
    if chessDict.values('bking') > 1:
        return False
    elif chessDict.values('wking') > 1:
        return False
    elif chessDict.items() > 32:
        return False
    elif chessDict.values('bpawn') > 8:
        return False
    elif chessDict.values('wpawn') > 8:
        return False
    elif chessDict.keys(
