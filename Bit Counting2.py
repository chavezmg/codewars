#Bit Counting2

def count_bits(n):
    binary = []
    counter = 0
    if n == 1:
        binary.append(1)
        return 1
    elif n == 0:
        return 0
    while n != 1:
        binary.append((n%2))
        if (n%2) == 1:
            counter += 1
        n = int(n/2)
        if n == 1:
            binary.append(1)
            counter += 1
            break
    binary.reverse()
    return counter

print(count_bits(0))