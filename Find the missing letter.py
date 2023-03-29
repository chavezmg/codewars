#Find the missing letter

def find_missing_letter(chars):
    dic1 = "abcdefghijklmnopqrstuvwxyz"
    chars = "".join(chars)
    first_char = chars[0]
    last_char = chars[len(chars)-1]
    upper = first_char.isupper()
    index_first_char, index_last_char = int(), int()
    converted = dict()

    if upper:
        index_first_char = dic1.upper().index(first_char)
        index_last_char = dic1.upper().index(last_char)
    else:
        index_first_char = dic1.index(first_char)
        index_last_char = dic1.index(last_char)
        
    for i, j in zip(dic1[index_first_char:index_last_char], chars):
        if chars.isupper():
            converted[i.upper()] = j
        else:
            converted[i] = j  

    for i,j in converted.items():
        if i != j:
            return i
  

test1= ["a", "c", "d", "e", "f"]
test2= ["B","C","D","E","F","H"]

print(find_missing_letter(test1))
print(find_missing_letter(test2))