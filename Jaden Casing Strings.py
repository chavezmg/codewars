#Jaden Casing Strings

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