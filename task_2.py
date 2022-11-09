import random
from turtle import *

def inflacja():
  return random.randint(30,60)  


def rok2022():
  result = []
  for i in range(12):
    result.append(inflacja() + 5 * i)
  return result


print(rok2022())


speed("very slow")

def wykres_inflacji(rok):
    for i in rok:
        left(90)
        forward(i)
        right(90)
        forward(5)
        right(90)
        forward(i)
        left(90)
        backward(5)
        forward(5)
        penup()
        forward(5)
        pendown()


rok = rok2022()
wykres_inflacji(rok)
print(rok2022())

exitonclick()
