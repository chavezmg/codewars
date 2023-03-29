#Find The Parity Outlier

def find_outlier(integers):
    odd = 0
    even = 0
    resulteven, resultodd = 0, 0
    for i in integers:
        if (i%2) == 0:
            even += 1
            resulteven = i
        else:
            odd += 1
            resultodd = i
    if odd > even:
        return resulteven
    else:
        return resultodd

a = [1,3,5,7,9,11,13,14,15,17]
b = [2,4,6,7,8,10,12,14,16,18]
print(find_outlier(a))
print(find_outlier(b))