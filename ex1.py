from datetime import datetime


def ex1(name, age):
    text = "Hi " + name + "!\n you gonna have 100 years in the year of "
    yearHave = str((datetime.now().year - age)+100)
    text += yearHave
    return text

# def ex2():



def test_ex1():
    name = "Rogerinho"
    age = 10
    assert ex1(name, age) == "Hi Rogerinho!\n you gonna have 100 years in the year of 2115"
    name1 = "Barbierry"
    age1 = 20
    assert ex1(name1,age1) == "Hi Barbierry!\n you gonna have 100 years in the year of 2105"