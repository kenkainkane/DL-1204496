import sys
import numpy as np

def gate(n):
    if n == 'and':
        tbl = np.array([[0, 0, 0],
                [0, 1, 0],
                [1, 0, 0],
                [1, 1, 1]], np.int8)
    elif n == 'or':
        tbl = np.array([[0, 0, 0],
                [0, 1, 1],
                [1, 0, 1],
                [1, 1, 1]], np.int8)
    elif n == 'xor':
        tbl = np.array([[0, 0, 0],
                [0, 1, 1],
                [1, 0, 1],
                [1, 1, 0]], np.int8)
    return tbl

def calculate(tbl):
    b, w1, w2 = (0, 0, 0)
    count = 0
    check = 0
    while (check < 4) and (count < 100000):
        row = count%4
        sop = b + w1*tbl[row][0] + w2*tbl[row][1]
        y = tbl[row][2]
        if (sop <= 0) and (y == 0):
            check+=1
        elif (sop > 0) and (y == 0):
            b = b - 1
            w1 = w1 - tbl[row][0]
            w2 = w2 - tbl[row][1]
            check = 0
        elif (sop >= 1) and (y == 1):
            check+=1
        elif (sop < 1) and (y == 1):
            b = b + 1
            w1 = w1 + tbl[row][0]
            w2 = w2 + tbl[row][1]
            check = 0
        count+=1
    if check == 4:
        return [b, w1, w2]
    else :
        return 'Need Multilayer Perceptron'

print(calculate(gate(sys.argv[1])))