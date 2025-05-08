from datetime import datetime

def ex1(name, age):
    text = "Hi " + name + "!\n you gonna have 100 years in the year of "
    yearHave = str((datetime.now().year - age)+100)
    text += yearHave
    return text
def ex2(int):
    if int%2==0:
        return "Even"
    else:
        return "Odd"
def ex3(list, maior):
    devolve = []
    for num in list:
        if num<maior:
            devolve.append(num)
    return devolve
def ex4(numerador):
    divisores = []
    divisor = numerador-1
    while divisor > 0:
        if numerador%divisor==0:
            divisores.append(divisor)
        divisor = divisor-1
    return sorted(divisores)
def ex5(listA, listB):
    comum = []
    for num in listA:
        if num in listB:
            if num not in comum:
                comum.append(num)
    return comum
def ex6(text):
    text = text.lower()
    textR = text[::-1]
    return text == textR