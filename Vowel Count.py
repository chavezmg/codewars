#Vowel Count

def get_count(sentence):
    vowels = ["a","e","i","o","u"]
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    return count

test1 = ["a","e","i","i","o"] #5 vowels
test2 = ["a","b","c"," ","e","o"] #3 vowels
test3 = [" ","a","a","u"," ", "u","x","x","o","e"] #6 vowels

print(get_count(test1))
print(get_count(test2))
print(get_count(test3))