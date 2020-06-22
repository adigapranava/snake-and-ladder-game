import turtle
import random
import time

#Some constants
X=40
Y=40
STARTx = -200-40
STARTy  = -200
TURN = 0 
SCOREP1 = 0
SCOREP2 = 0
OLD_CLICKS = 0
NEW_CLICKS = 1 
END = 100
JUST_STARTED1 = True
JUST_STARTED2 = True
CHANGED1 = False
CHANGED2 = False

#setting my screen
screen = turtle.Screen()
screen.bgpic("Snakes-And-Ladders-Board.gif")
screen.setup(420,420) 

#1st players initial setup
p1 = turtle.Turtle()
p1.shape("turtle")
p1.color("black")
p1.speed(1)
p1.penup()
p1.setpos(STARTx + X/2, STARTy +Y/2)

#2nd players initial setup
p2 = turtle.Turtle()
p2.shape("turtle")
p2.color("violet")
p2.speed(1)
p2.penup()
p2.setpos(STARTx + X/2, STARTy +Y/2)

#returns a result of rolling a die
def rolling():
    n= random.randint(1,10000)
    print(n%5 + 1)
    return n%5 + 1

#when spacebar is pressed it runs only after the complition of previous step
def rolled():
	global TURN, FORWARD1, FORWARD2, SCOREP1, SCOREP2, OLD_CLICKS, NEW_CLICKS, JUST_STARTED1, CHANGED1, JUST_STARTED2, CHANGED2
	die = rolling()
	if TURN%2 == 0 and OLD_CLICKS != NEW_CLICKS: #2nd condition is to check if the previous step is successfully compleated
		OLD_CLICKS = NEW_CLICKS
		for _ in range(die):
			if p1.pos()[0] > 200-X and CHANGED1 is False:  #1st cond to check the last position and 2nd condition is to check if the position is changed
				p1.goto(p1.pos()[0], p1.pos()[1] + Y)
				p1.setheading(180)
				CHANGED1 = True
				continue
			elif p1.pos()[0] < -200 + X  and JUST_STARTED1 is False and CHANGED1 is False: 
				p1.goto(p1.pos()[0], p1.pos()[1] + Y)
				p1.setheading(0)
				CHANGED1 = True
				continue
			p1.forward(X)
			CHANGED1 = False
		SCOREP1 += die
		print("p1",SCOREP1)
		TURN += 1
		NEW_CLICKS += 1
		if SCOREP1 != 1:
			JUST_STARTED1 = False
	elif TURN%2 == 1 and OLD_CLICKS != NEW_CLICKS:  	#player 2
		OLD_CLICKS = NEW_CLICKS
		for _ in range(die):
			if p2.pos()[0] > 200-X and CHANGED2 is False: 
				p2.goto(p2.pos()[0], p2.pos()[1] + Y)
				p2.setheading(180)
				CHANGED2 = True
				continue
			elif p2.pos()[0] < -200 + X  and JUST_STARTED2 is False and CHANGED2 is False: 
				p2.goto(p2.pos()[0], p2.pos()[1] + Y)
				p2.setheading(0)
				CHANGED2 = True
				continue
			p2.forward(X)
			CHANGED2 = False
		SCOREP2 += die
		print("p2",SCOREP2)
		TURN += 1
		NEW_CLICKS += 1
		if SCOREP2 != 1:
			JUST_STARTED2 = False



turtle.listen()
turtle.onkey(rolled,"space")
turtle.mainloop()
