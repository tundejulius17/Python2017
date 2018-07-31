#a program which fires with f and quits with q
import turtle
import time

screen = turtle.Screen()
t = turtle.Turtle()


def fire():
 x = -400
 y = -350

 for i in range(70):
  t.setx(x)
  t.sety(y)
  t.dot(10, 'red')
  x += 10
  y += 10


 for i in range(100):
    t.goto(x, -350)
    t.dot(10, 'red')



def quit():
  turtle.bye()


ch = input('enter f to fire or q to quit !')

if ch == 'f':
    fire()
elif ch == 'q':
    quit()
