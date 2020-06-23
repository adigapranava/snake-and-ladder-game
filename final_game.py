import turtle
import random
import time

#Some constants
X=40
Y=40
STARTx = -200-X
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
END = 100
PERMISSION1 = True
PERMISSION2 = True

def check_ladder(p):
    if p == 1:
        print("Ladder!!")
        return 38
    elif p == 4:
        print("Ladder!!")
        return 14
    elif p == 9:
        print("Ladder!!")
        return 31
    elif p == 21:
        print("Ladder!!")
        return 42
    elif p == 28:
        print("Ladder!!")
        return 84
    elif p == 51:
        print("Ladder!!")
        return 67
    elif p == 72:
        print("Ladder!!")
        return 91
    elif p == 80:
        print("Ladder!!")
        return 99
    else:
        return p

def check_snake(p):
    if p == 17:
        print("Snake!!")
        return 7
    elif p == 54:
        print("Snake!!")
        return 34
    elif p == 62:
        print("Snake!!")
        return 19
    elif p == 64:
        print("Snake!!")
        return 60
    elif p == 87:
        print("Snake!!")
        return 36
    elif p == 93:
        print("Snake!!")
        return 73
    elif p == 95:
        print("Snake!!")
        return 75
    elif p == 98:
        print("Snake!!")
        return 79
    else:
        return p

#setting my screen
screen = turtle.Screen()
screen.bgpic("Snakes-And-Ladders-Board.gif")
screen.setup(420,420) 

#
p1 = turtle.Turtle()
p1.shape("turtle")
p1.color("black")
p1.speed(0)
p1.penup()
p1.setpos(STARTx + X/2, STARTy +Y/2)
p1.speed(1)

p2 = turtle.Turtle()
p2.shape("turtle")
p2.color("violet")
p2.speed(0)
p2.penup()
p2.setpos(STARTx + X/2, STARTy +Y/2)
p2.speed(1)

def position1(SCOREP1):
    if SCOREP1//10 % 2 == 0 and SCOREP1%10 != 0:
        p1.goto(STARTx + X/2+ SCOREP1%10 * X, STARTy - Y/2 + (SCOREP1//10 + 1) * Y)
        p1.setheading(0)
    elif SCOREP1//10%2 == 1 and SCOREP1%10 != 0:
        p1.goto(STARTx + 3*X/2 + (10 - SCOREP1%10) * X, STARTy - Y/2 + (SCOREP1//10 + 1) * Y)
        p1.setheading(180)
    elif SCOREP1//10 % 2 == 0 and SCOREP1%10 == 0:
        p1.goto(STARTx + 3*X/2+ SCOREP1%10 * X, STARTy - 3*Y/2 + (SCOREP1//10 + 1) * Y)
        p1.setheading(180)
    elif SCOREP1//10%2 == 1 and SCOREP1%10 == 0:
        p1.goto(STARTx + X/2 + (10 - SCOREP1%10) * X, STARTy - 3*Y/2 + (SCOREP1//10 + 1) * Y)
        p1.setheading(0)

def position2(SCOREP1):
    if SCOREP1//10 % 2 == 0 and SCOREP1%10 != 0:
        p2.goto(STARTx + X/2+ SCOREP1%10 * X, STARTy - Y/2 + (SCOREP1//10 + 1) * Y)
        p2.setheading(0)
    elif SCOREP1//10%2 == 1 and SCOREP1%10 != 0:
        p2.goto(STARTx + 3*X/2 + (10 - SCOREP1%10) * X, STARTy - Y/2 + (SCOREP1//10 + 1) * Y)
        p2.setheading(180)
    elif SCOREP1//10 % 2 == 0 and SCOREP1%10 == 0:
        p2.goto(STARTx + 3*X/2+ SCOREP1%10 * X, STARTy - 3*Y/2 + (SCOREP1//10 + 1) * Y)
        p2.setheading(180)
    elif SCOREP1//10%2 == 1 and SCOREP1%10 == 0:
        p2.goto(STARTx + X/2 + (10 - SCOREP1%10) * X, STARTy - 3*Y/2 + (SCOREP1//10 + 1) * Y)
        p2.setheading(0)

def rolling():
    n= random.randint(1,10000)
    print(n%5 + 1)
    return n%5 + 1


def rolled():
    global TURN, FORWARD1, FORWARD2, SCOREP1, SCOREP2, OLD_CLICKS, NEW_CLICKS, JUST_STARTED1, CHANGED1, JUST_STARTED2, CHANGED2, PERMISSION1, PERMISSION2
    die = rolling()
    PERMISSION1 = True
    PERMISSION2 = True
    if SCOREP1 + die > 100 and TURN%2 == 0:
            print("you cant exceed 100 :)")
            PERMISSION1 = False
    if SCOREP2 + die > 100 and TURN%2 == 1:
            print("you cant exceed 100 :)")
            PERMISSION2 = False
    if TURN%2 == 0 and OLD_CLICKS != NEW_CLICKS and PERMISSION1 == True:            
        OLD_CLICKS = NEW_CLICKS
        for _ in range(die):
            if p1.pos()[0] > 200-X and CHANGED1 is False: 
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
        #check for ladder or snake here
        SCOREP1 = check_snake(SCOREP1)
        SCOREP1 = check_ladder(SCOREP1)
        position1(SCOREP1)
        print("p1",SCOREP1)
        NEW_CLICKS += 1
        if SCOREP1 != 1:
            JUST_STARTED1 = False
    elif TURN%2 == 1 and OLD_CLICKS != NEW_CLICKS and PERMISSION2 == True:          #player 2
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
        #check for ladder or snake here
        SCOREP2 = check_snake(SCOREP2)
        SCOREP2 = check_ladder(SCOREP2)
        position2(SCOREP2)
        print("p2",SCOREP2)
        NEW_CLICKS += 1
        if SCOREP2 != 1:
            JUST_STARTED2 = False
    TURN += 1


turtle.listen()
turtle.onkey(rolled,"space")
turtle.mainloop()
