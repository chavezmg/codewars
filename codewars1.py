#presiona ctrl-f y busca "incompleto" para buscar los katas sin terminar


#kata feynman square equation - incompleto
""" Solucion 1
def count_squares(n):
    if n*n == 1:
        return 1
    return count_squares(n-1) + n*n

print(count_squares(6))
"""
""" Solucion 2
def count_squares(n):
    suma = 0
    for i in range(n+1):
        suma += i*i
    return suma

print(count_squares(12))
"""
""" Solucion 3
def count_squares(n):
    result = int((n*(n+1)*(2*n+1))/6)
    return result

print(count_squares(7))
"""

#KATA bingo
"""
def bingo(array): 
    win = [2, 9, 14, 7, 15]
    for i in win:
        if i not in array:
            return "LOSE"
    return "WIN"

arra = [2,14,7,9,16,4,3,1]

print(bingo(arra))"""

#Sort numbers
"""
def solution(nums):
    min = 0
    if nums != None:
        nums.sort()
    else:
        return []
    return nums
s = [5,4,3,2,1]
print(solution(s))
"""
#Find the vowels
"""
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
"""

#Credit card mask
"""
def maskify(cc):
    result = str()
    for i in cc[:-4]:
        result += "#"
    for i in cc[-4:]:
        result += i 
    return result

print (maskify("perro sucio sidroso"))
"""

#Kill the monsters!
"""
def kill_monsters(health, monsters, damage):
    if (monsters % 3) == 0:
        hits = int(monsters/3)-1
    else:
        hits = int(monsters/3)
    dmg = int(hits * damage)
    hp = int(health - dmg)
    if hp <= 0:
        return "hero died"
    return f"hits: {hits}, damage: {dmg}, health: {hp}"

print(kill_monsters(10, 7, 5))
"""

#Disemvowel Trolls
"""
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
"""

#WeIrD StRiNg CaSe
"""
def to_weird_case(string):
    result = []
    j = 2 #even
    for i in string:
        if (j%2) == 0:
            result.append(i.upper())
            j = 1 #odd
        elif (j%2) != 0:
            result.append(i.lower())
            j = 2 #even
        if i == " ":
            j = 2 #even
    result = "".join(result)
    return result

s = "this is a test"
print(to_weird_case(s))
"""

#Isograms
"""
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
"""

#Find The Parity Outlier
"""
def find_outlier(integers):
    odd = 0
    even = 0
    resulteven, resultodd = 0, 0
    for i in integers:
        if (i%2) == 0:
            even += 1
            resulteven = i
        else:
            odd += 1
            resultodd = i
    if odd > even:
        return resulteven
    else:
        return resultodd

a = [1,3,5,7,9,11,13,14,15,17]
b = [2,4,6,7,8,10,12,14,16,18]
print(find_outlier(a))
print(find_outlier(b))
"""

#Multiples of 3 or 5
"""
def solution(number):
    result = 0
    if number < 0:
        return 0
    for i in range(1, number):
        if (i%3) == 0 or (i%5)==0:
            result += i
    return result
print(solution(20))
"""

#Bit Counting
"""
def count_bits(n):
    #binary = []
    counter = 0
    while n != 1:
    #    binary.append((n%2))
        if (n%2) == 1:
            counter += 1
        n = int(n/2)
        if n == 1:
    #        binary.append(1)
            counter += 1
            break
    #binary.reverse()
    return counter

print(count_bits(300))"""

#Bit Counting2
"""
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
"""

#Valid Parentheses   - incompleto
"""
def valid_parentheses(string):
    open_positions = []
    closed_positions = []
    #open = 0
    #closed = 0
    j = 0 
    for i in string:
        if i == "(":
            open_positions.append(j)
        elif i == ")":
            closed_positions.append(j)
        j += 1
    print(open_positions)
    print(closed_positions)


test1 = "()"
test2 = ")(()))"
test3 = "("
test4 = "(())((()())())"
print(valid_parentheses(test1))
print(valid_parentheses(test2))
print(valid_parentheses(test3))
print(valid_parentheses(test4))
"""

#Find the missing letter
"""
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
"""

#Vowel Count
"""
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
"""

#Counting Duplicates
"""
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
"""

#Jaden Casing Strings
"""
def to_jaden_case(string): #solucion 1
    result = []
    for i in string.split():
        result.append(i.capitalize())
    return " ".join(result)

test1 = "hola, me llamo Jaden Smith, capitalizo todo porque me gusta"
test2 = "mi papá trabajó en varias peliculas"

print(to_jaden_case(test1))
print(to_jaden_case(test2))
"""
"""
def to_jaden_case(string): #solucion 2
    result = str()
    string = string.split()
    for i in string:
        result += i.capitalize()
        result += " "
    return result.rstrip()
"""

#Value of x      incompleto
"""
def solve(eq):
    eq = eq.replace(" ", "")
    x_index = eq.index("x")
    equal_index = eq.index("=")
    result_right, result_left, result = 0, 0, 0
    pos,posns = 0, 0    #pos, posnextsymbol
    next_simbol_index = 0
        
    print(eq)
    ##Resolve equation in right side
    if eq[equal_index+1].isdigit():#check if theres a positive number bigger than 9 starting after the '='
        for k in eq[equal_index+1:]:
                if k == "-" or k == "+":
                    next_simbol_index = eq[equal_index+1:].index(k)
                    print("next simbol index is", next_simbol_index)
                    break
        result_right += int(eq[equal_index+1:equal_index+1+next_simbol_index])
    posi = next_simbol_index
    for i in eq[equal_index+1+posi: ]:
        if (i == "-" or i == "+") and eq[(equal_index+pos+2)] != "x":
            posns = 0
            for k in eq[equal_index+1+pos+1+posi:]:
                if k == "-" or k == "+":
                    next_simbol_index = eq[equal_index+posi+pos+posns:].index(k)
                    print("next simbol index is", next_simbol_index)
                    break
                posns += 1
            if i == "-":
                print("hola ", eq[equal_index+posi+pos+1+posns:equal_index+pos+posi+next_simbol_index+pos+1]) 
                result_right -= int(eq[equal_index+posi+pos+1+posns:equal_index+pos+posi+next_simbol_index+pos+1])
            else:
                result_right += int(eq[equal_index+posi+pos+1+posns:equal_index+pos+posi+next_simbol_index+pos+1])
        pos += 1

    ##Resolve equation in left side BIEN
    pos = 0
    if eq[0].isdigit():
        result_left += int(eq[0])
    for i in eq[:equal_index]:
        if (i == "-" or i == "+") and eq[(pos+1)] != "x":                                #
            for k in eq[(pos+1):equal_index+1]:
                if k == "-" or k == "+" or k == "=":
                    next_simbol_index = eq[pos+1:equal_index+1].index(k) +1                             #
            if i == "-":
                result_left -= int(eq[(pos+1):next_simbol_index])
            else:
                result_left += int(eq[(pos+1):next_simbol_index])
        pos += 1
     
    if equal_index > x_index: #X is on the left side
        result = result_right - result_left
    else:                     #X is on the right side
        result = result_left - result_right
    
    if eq[x_index-1] == "-":
        result = -result

    print(eq)
    print(x_index, equal_index)
    print("Right result is: ", result_right)
    print("Left result is: ", result_left)
    print("Total result is: ", result)

#test1 = 'x + 1 = 9 - 2 + 4 + 3'  #result is 14
test2 = '- 10 = 5 - 4 + 5 + x'               #result is -10
#test3 = 'x - 2 + 3 = 2'          #result is 1
#test4 = '- x = - 1'              #result is 1
#print(solve(test1))
print(solve(test2))
#print(solve(test3))
#print(solve(test4))"""


#RGB To Hex Conversion
"""from math import floor
def conversor(value):
    remain = value
    result_dec = list()
    
    if remain == 0:
        result_dec.append(0)
    while remain > 0:
        result_dec.append(remain%16)
        remain = floor(remain/16)
    result_dec.reverse()
    print(result_dec)

    j=0
    for i in result_dec:
        if i==15:
            result_dec[j]="F"
        elif i==14:
            result_dec[j]="E"
        elif i==13:
            result_dec[j]="D"
        elif i==12:
            result_dec[j]="C"
        elif i==11:
            result_dec[j]="B"
        elif i==10:
            result_dec[j]="A"

        if i>0 and i<10 and len(result_dec)==1:     #   
            result_dec[j] = "0" + str(i) 
        elif i>0 and i<10 and len(result_dec)>1:        
            result_dec[j] = str(i)       
        elif i == 0 and len(result_dec)==1:
            result_dec[j] = "00"
        j+=1

    result_dec = "".join(result_dec)
    return result_dec

def rgb(r, g, b):
    if r>255:
        r=255
    elif r<0:
        r=0
    if g>255:
        g=255
    elif g<0:
        g=0    
    if b>255:
        b=255
    elif b<0:
        b=0
    
    result_r = conversor(r)
    result_g = conversor(g)
    result_b = conversor(b)
    return(result_r+result_g+result_b)

print(rgb (97,288,-110))"""


#Where is my parent!?(cry)
"""def find_children(dancing_brigade):
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

#Remove String Spaces
"""def no_space(x):
    return(x.replace(" ", ""))
print(no_space("hola me llamo matias"))"""

#String cleaning
"""def string_clean(s):
    print(s)
    result = "".join(i for i in s if i.isnumeric()== False)
    return result
print(string_clean("ho0la232 me llamo ma34tias"))"""

#Prostate cancer recurrence rates (ASTRO)
"""def recurrence(values):
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
print(recurrence([14.66, 3.14, 0.53, 0.58, 1.00, 1.26, 0.99 ,2.1, 1.50, 2.53, 2.17, 2.50]))"""

#Delete occurrences of an element if it occurs more than n times
"""def delete_nth(order,max_e):
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
print(delete_nth([20,37,20,21], 1))"""

#Holiday VI - Shark Pontoon
"""def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed /= 2
    shark_time = shark_distance/shark_speed
    you_time = pontoon_distance/you_speed
    
    if shark_time < you_time:
        return "Shark Bait!"
    else:
        return "Alive!"""

#Simple Fun #217: Sort By Guide
def sort_by_guide(arr, guide):
    order = dict()
    no_order = dict()
    result = list()
    x = 0
    for i,j in zip(arr,guide):
        if j == -1:
            no_order[x] = i
        elif j != -1:
            order[j] = i
        x += 1

    for i in range(1, len(order)+1):
        result.append(order[i])
    for i in no_order:
        result.insert(i, no_order[i])

    return result

print(sort_by_guide([56, 78, 3, 45, 4, 66, 2, 2, 4], [3, 1, -1, -1, 2, -1, 4, -1, 5]))
