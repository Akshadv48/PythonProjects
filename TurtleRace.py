from turtle import *
from random import randint


def turt():
	tur1 = Turtle()
	tur1.color('red')
	tur1.shape('turtle')
	tur1.penup()
	tur1.goto(-160,120)
	tur1.pendown()
###############Turtle 2############
	tur2 = Turtle()
	tur2.color('blue')
	tur2.shape('turtle')
	tur2.penup()
	tur2.goto(-160,60)
	tur2.pendown()
###############Turtle 3############
	tur3 = Turtle()
	tur3.color('green')
	tur3.shape('turtle')
	tur3.penup()
	tur3.goto(-160,0)
	tur3.pendown()
##############Turtle 4#############
	tur4 = Turtle()
	tur4.color('black')
	tur4.shape('turtle')
	tur4.penup()
	tur4.goto(-160,-60)
	tur4.pendown()
#****************for loop to make turtle run****************
	for i in range(120):
		tur1.forward(randint(1,5))
		tur3.forward(randint(1,5))
		tur4.forward(randint(1,5))
		tur2.forward(randint(1,5))


def main():
	penup()
	speed(0)
	goto(-140,140)
	for step in range(15):
		write(step, align='center')
		right(90)
		forward(10)
		pendown()
		speed(0)
		for i in range(20):

			forward(5)
			penup()
			forward(5)
			pendown()
		penup()
		backward(210)
		left(90)
		forward(20)
	penup()
	forward(25)
	right(90)
	write("FINISH")
	pendown()
	forward(210)
	penup()
	backward(210)
	turt()
	done()

if __name__ == '__main__':
	main()