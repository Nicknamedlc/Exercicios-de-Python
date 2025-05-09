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
def ex7(list):
    return [num for num in list if num %2==0]
def ex8(jog1, jog2):
    jog1 = jog1.lower()
    jog2 = jog2.lower()
    if jog1 == jog2:
        return "empate"
    else:
        if (jog1 == "tesoura" and jog2 == "pedra") or (jog1 == "pedra" and jog2 == "tesoura"):
            return "Pedra ganha de tesoura"
        elif (jog1 == "tesoura" and jog2 == "papel") or (jog1 == "papel" and jog2 == "tesoura"):
            return "Tesoura ganha de papel"
        else:
            return "Papel ganha de pedra"