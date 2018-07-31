import turtle
import time
screen = turtle.Screen()


s=turtle.Screen()
t=turtle.Turtle()
t.hideturtle()
t.penup()
t.setx(-20)
t.sety(-120)
t.pendown()
t.pensize(3)
t.circle(100)
t.penup()
t.setx(0)
t.sety(0)
t.setx(-50)
t.setheading(150)
t.pendown()
t.circle(50, 60)
t.penup()
#Here we set coordinates for left eye
t.setx(-75)
t.sety(-10)
t.pendown()
#Here we draw left eye
t.dot(10)
t.penup()
#Here we draw the right eyebrow
t.setx(50)
t.sety(0)
t.setheading(150)
t.pendown()
t.circle(50, 60)
#Here we draw the right eye
t.penup()
t.setx(25)
t.sety(-10)
t.pendown()
t.dot(10)
#Here we draw the nose
t.penup()
t.setx(-20)
t.sety(-20)
t.pendown()
t.pensize(5)
t.goto(-20,-50)
#Here we draw the mouth
t.penup()
t.setx(-27)
t.sety(-80)
t.setheading(0)
t.pendown()
t.circle(90, 10)
#Animation control
for i in range(1000):
    turtle.stamp()
    turtle.update()
    time.sleep(3)
