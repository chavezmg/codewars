#Counting Duplicates

def duplicate_count(text):
    text = text.lower()
    text = list(text)
    repeats = set()
    j = 0

    for i in text:
        if i in text[j+1:]:
            repeats.add(i)
        j += 1
    return len(repeats)

test1 = "" #debe retornar 0
test2 = "abcde" #debe retornar 0
test3 = "abcdeaa" #debe retornar 1
test4 = "abcdeaB"      #debe retornar 2
test5 = "Indivisibilities" #debe retornar 2

print(duplicate_count(test1))
print(duplicate_count(test2))
print(duplicate_count(test3))
print(duplicate_count(test4))
print(duplicate_count(test5))