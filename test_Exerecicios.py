import Exerecicios


def test_ex1():
    name = "Rogerinho"
    age = 10
    assert Exerecicios.ex1(name, age) == "Hi Rogerinho!\n you gonna have 100 years in the year of 2115"
    name1 = "Barbierry"
    age1 = 20
    assert Exerecicios.ex1(name1,age1) == "Hi Barbierry!\n you gonna have 100 years in the year of 2105"

def test_ex2():
    assert Exerecicios.ex2(5) == "Odd"
    assert Exerecicios.ex2(10) == "Even"
    assert Exerecicios.ex2(0) == "Even"
def test_ex3():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert Exerecicios.ex3(a,6) == [1, 1, 2, 3, 5]
    assert Exerecicios.ex3(a,10) == [1, 1, 2, 3, 5, 8]
    assert Exerecicios.ex3(a,1) == []
def test_ex4():
    numerador = 4
    assert Exerecicios.ex4(numerador) == [1,2]
    numerador = 50
    assert Exerecicios.ex4(numerador) == [1, 2, 5, 10, 25]
def test_ex5():
    listA = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    listB = [2,4,6,8,10,12,14,16]
    assert Exerecicios.ex5(listA,listB) == [2,4,6,8,10,12]

    listA = [1,2,5,9,7,5,3,4,5,6]
    listB = [2,4,6,8,10,12,14,16]
    assert Exerecicios.ex5(listA,listB) == [2,4,6]
def test_ex6():
    assert Exerecicios.ex6("arara") == True