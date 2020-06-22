import turtle
import random
import time

X=40
Y=40
STARTx = -200-40
STARTy  = -200
TURN = 0 
FORWARD1 = True
FORWARD2 = True
SCOREP1 = 0
SCOREP2 = 0
OLD_CLICKS = 0
NEW_CLICKS = 1 

screen = turtle.Screen()
screen.bgpic("Snakes-And-Ladders-Board.gif")
screen.setup(420,420) 

p1 = turtle.Turtle()
p1.shape("turtle")
p1.color("black")
p1.speed(1)
p1.penup()
p1.setpos(STARTx + X/2, STARTy +Y/2)

p2 = turtle.Turtle()
p2.shape("turtle")
p2.color("violet")
p2.speed(1)
p2.penup()
p2.setpos(STARTx + X/2, STARTy +Y/2)

def rolling():
    n= random.randint(1,10000)
    print(n%5 + 1)
    return n%5 + 1

def rolled():
	global TURN, FORWARD1, FORWARD2, SCOREP1, SCOREP2, OLD_CLICKS, NEW_CLICKS
	die = rolling()
	if TURN%2 == 0 and OLD_CLICKS != NEW_CLICKS:
		OLD_CLICKS = NEW_CLICKS
		for _ in range(die):
			if p1.pos()[0] > 200-X and FORWARD1 == True or p1.pos()[0] < -200 + X and FORWARD1 == False: 
				p1.goto(p1.pos()[0], p1.pos()[1] + Y)
				if FORWARD1 == True:
					FORWARD1 = False
				else:
					FORWARD1 = True
				continue
			if FORWARD1 == True:
				p1.forward(X)
			else:
				p1.backward(X)
		SCOREP1 += die
		print("p1",SCOREP1)
		TURN += 1
		NEW_CLICKS += 1
	elif TURN%2 == 1 and OLD_CLICKS != NEW_CLICKS:
		OLD_CLICKS = NEW_CLICKS
		for _ in range(die):
			if p2.pos()[0] > 200-X and FORWARD2 == True or p2.pos()[0] < -200 + X and FORWARD2 == False: 
				p2.goto(p2.pos()[0], p2.pos()[1] + Y)
				if FORWARD2 == True:
					FORWARD2 = False
				else:
					FORWARD2 = True
				continue
			if FORWARD2 == True:
				p2.forward(X)
			else:
				p2.backward(X)
		SCOREP2 += die
		print("p2",SCOREP2)
		TURN += 1
		NEW_CLICKS += 1



turtle.listen()
turtle.onkey(rolled,"space")
turtle.mainloop()