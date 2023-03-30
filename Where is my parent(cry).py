#Where is my parent(cry)
def find_children(dancing_brigade):
    #parents = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    parents, children, result = list(), list(), list()

    for i in dancing_brigade:
        if i.isupper():
            parents.append(i)
        elif i.islower():
            children.append(i)
    parents.sort()
    children.sort()

    for i in parents:
        if i.lower() in children:
            result.append(i + children.count(i.lower())*i.lower())
        else:
            result.append(i)
    result = "".join(result)
    return result

print(find_children("abBA"))
print(find_children("AaaaaZazzz"))
print(find_children("CbcBcbaA"))
print(find_children("xXfuUuuF"))
print(find_children("faCdxwbsaQexfjaDsaxmnmyaAaZyunwSdeqkaenhUJYebqzumlHewwlukMqegKqleedwkrskjWdFXdxzBxwwGdNwxjjVqRLsEkk"))"""
