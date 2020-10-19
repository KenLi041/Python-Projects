def p1(i):
    i = 0
    while i < 10:
        if i % 5 == 0:
            print(i)
        if i % 10 == 0:
            print(i**2)
        i += 1
    else: print("not valid")
    
def alternative(i):
    for i in range(0, 10, 5):
        print(i)
    else: print("not valid")


def decimal_to_binary(q):
    binary = ''
    while (q != 0):
        r = q % 2
        q = q // 2
        binary = str(r) + binary
    return binary
    print (binary)

def make_HTML_element (tag, word):
    frontTag = "<"
    backTag = "</"
    for i in range(len(tag)): 
        frontTag += tag[i]
        backTag+= tag[i]
    frontTag += ">"
    backTag += ">"
    html = frontTag + word + backTag
    print (html)
def mystery(x):
    y = str(x)
    if int(y[1]) > 5 and int(y[2]) < 10:
        print (y[0] * 2)
    elif type(y) == str:
        print (int(y[1]) **3)
    else: print ("not valid") 