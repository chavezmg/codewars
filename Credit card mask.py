#Credit card mask

def maskify(cc):
    result = str()
    for i in cc[:-4]:
        result += "#"
    for i in cc[-4:]:
        result += i 
    return result

print (maskify("perro sucio sidroso"))