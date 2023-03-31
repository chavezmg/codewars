#Prostate cancer recurrence rates (ASTRO)
def recurrence(values):
    min_value_index = values.index(min(values))
    rises, j = 0, min_value_index
    for i in values[(min_value_index):]:
        if rises>2:
            return True
        if(j<len(values)-1):
            if values[j] < values[j+1]:
                rises += 1
            else:
                rises = 0
        j += 1
    return False
    
print(recurrence([7.91, 2.43, 1.49, 0.99, 0.74, 0.48, 0.52, 0.50, 0.66, 1.26, 1.36, 1.35]))
print(recurrence([9.98, 8.56, 4.62, 1.16, 0.26, 0.37, 0.32, 1.02, 1.02, 0.99, 1.41, 2.35]))
print(recurrence([14.66, 3.14, 0.53, 0.58, 1.00, 1.26, 0.99 ,2.1, 1.50, 2.53, 2.17, 2.50]))