#Find the vowels

def vowel_indices(word):
    vowels = ["a","e","i","o","u","y"]
    result = []
    j = 0
    word = word.lower()
    for i in word:
        j += 1
        if i in vowels:
            result.append(j)
    return result

print (vowel_indices("spicery"))
