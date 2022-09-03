import turtle
obj=turtle.Turtle()

obj.speed(10)

list01=["yellow","red","green","blue","orange"]

for i in range(200):
    obj.color(list01[1%5])
    obj.pensize(i/10+1)
    obj.forward(i)
    obj.left(90)

obj.left(90)
obj.pencolor("green")
obj.pensize(5)

def tree(L):
	if(l<10):
		return
	else:
		obj.forward(l)
		obj.left(30)
		tree(3*i/4)
		obj.right(60)
		tree(3*1/4)
		obj.left(30)
		obj.backward(1)

tree(100)

turtle.done()

==
import turtle
obj=turtle.Turtle()

obj.speed(10)

list01=["yellow","red","green","blue","orange"]

for i in range(200):
    obj.color(list01[1%5])
    obj.pensize(i/10+1)
    obj.forward(i)
    obj.left(59)
===
import turtle

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(500)

draw_circle(tommy, "green", 50, 25, 0)
draw_circle(tommy, "blue", 50, 0, 0)
draw_circle(tommy, "yellow", 50, -25, 0)
===
go(50)
turn(90)
go(200)
