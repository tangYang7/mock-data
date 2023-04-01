import json
from random import choice
def createIDcard():
    numbers = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    idnum_json = {
        "A": 10, "B": 11,
        "C": 12, "D": 13,
        "E": 14, "F": 15,
        "G": 16, "H": 17,
        "I": 34, "J": 18,
        "K": 19, "L": 20,
        "M": 21, "N": 22,
        "O": 35, "P": 23,
        "Q": 24, "R": 25,
        "S": 26, "T": 27,
        "U": 28, "V": 29,
        "W": 32, "X": 30,
        "Y": 31, "Z": 33
    }
    idHead = choice(letters)
    sum = 0
    sum += idnum_json[idHead]//10 + (idnum_json[idHead] %10) * 9

    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num[0] = choice([1,2])
    sum += num[0] * 8
    for i in range(1,8):
        num[i] = choice(numbers)
        sum += num[i] * (8-i)
    num[8] = 10 - sum%10
    sum += num[8]
# output
    numStr = ""
    for i in range(9):
        numStr += str(num[i])

    return idHead+numStr
