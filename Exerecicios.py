from datetime import datetime


def ex1(name, age):
    text = "Hi " + name + "!\n you gonna have 100 years in the year of "
    year_have = str((datetime.now().year - age) + 100)
    text += year_have
    return text


def ex2(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


def ex3(lista, maior):
    devolve = []
    for num in lista:
        if num < maior:
            devolve.append(num)
    return devolve


def ex4(numerador):
    divisores = []
    divisor = numerador - 1
    while divisor > 0:
        if numerador % divisor == 0:
            divisores.append(divisor)
        divisor = divisor - 1
    return sorted(divisores)


def ex5(list_a, list_b):
    comum = []
    for num in list_a:
        if num in list_b:
            if num not in comum:
                comum.append(num)
    return comum


def ex6(text):
    text = text.lower()
    text_r = text[::-1]
    return text == text_r


def ex7(lista):
    return [num for num in lista if num % 2 == 0]


def ex8():
    op = input("""
        Jogatina
        
        para jogar digite jogar
        para sair digite sair
    """)
    while op != "sair":
        if op == "jogar":
            jog1 = cria_jogador()
            jog2 = cria_jogador()
            print(vencedor(jog1, jog2))
        op = input("""
        deseja jogar novamente?
        
        para jogar digite jogar
        para sair digite sair
        """)


def cria_jogador():
    jogador = input("""
        Jogador 1 escolha
        1 - Pedra
        2 - Papel
        3 - Tesoura
        """)
    while jogador != '1' and jogador != '2' and jogador != '3':
        jogador = input("""
            Jogador 1 escolha
            1 - Pedra
            2 - Papel
            3 - Tesoura
            """)
    return jogador


def vencedor(jog1, jog2):
    if jog1 == jog2:
        return "    empate"
    else:
        if (jog1 == "3" and jog2 == "1") or (jog1 == "1" and jog2 == "3"):
            return "    Pedra ganha de tesoura"
        elif (jog1 == "3" and jog2 == "2") or (jog1 == "2" and jog2 == "3"):
            return "    Tesoura ganha de papel"
        else:
            return "    Papel ganha de pedra"
