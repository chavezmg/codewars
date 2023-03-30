#KATA bingo

def bingo(array): 
    win = [2, 9, 14, 7, 15]
    for i in win:
        if i not in array:
            return "LOSE"
    return "WIN"

arra = [2,14,7,9,16,4,3,1]

print(bingo(arra))