#Delete occurrences of an element if it occurs more than n times
def delete_nth(order,max_e):
    repeats = dict()
    result = list()
    for i in order:
        if order.count(i)>max_e:
            repeats[i] = max_e
        else:
            repeats[i] = order.count(i)

    for i in order:
        if repeats[i] > 0:
            result.append(i)
            repeats[i] -= 1 
    return result

print(delete_nth([1,2,3,1,2,1,2,3,4], 2))
print(delete_nth([20,37,20,21], 1))