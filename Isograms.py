#Isograms

def is_isogram(string):
    j=0
    string = string.lower()
    for i in string:
        j += 1
        if i in string[j:]:
            return False
    return True
        
s1 = "is this an isogram?"
s2 = "thiSs"

print(is_isogram(s1))
print(is_isogram(s2))