#Disemvowel Trolls

def disemvowel(string_):
    vowels = ["a","e","i","o","u", "A", "E", "I", "O", "U"]
    result = []
    string_ = string_.lower()
    for i in string_:
        if i not in vowels:
            result.append(i)
    result = "".join(result)
    return result

s = "Hola, PROBANDO probando jeje."
print(disemvowel(s))