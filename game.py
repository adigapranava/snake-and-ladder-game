import turtle
import random
import time
from dataclasses import dataclass

#Some constants
CELL_WIDTH = 40
CELL_HEIGHT = 40
START_X = -200 + (CELL_WIDTH // 2)
START_Y  = -200 + (CELL_HEIGHT // 2)
ALLOW_TURN = True
TURN = True # Whether P1 has its turn
SCOREP1 = 0
SCOREP2 = 0
END = 100
LADDER_MAP = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    51: 67,
    72: 91,
    80: 99
}
SNAKE_MAP = {
    17: 7,
    54: 34,
    62: 19,
    64: 60,
    87: 36,
    93: 73,
    95: 75,
    98: 79
}

@dataclass
class Position_info:
    x: int
    y: int
    rot: int

    def to_vec(self) -> turtle.Vec2D:
        return turtle.Vec2D(self.x, self.y)

def check_ladder(pos: int) -> int:
    global LADDER_MAP

    if pos in LADDER_MAP:
        print("Ladder!!")
        return LADDER_MAP[pos]
    else:
        return pos

def check_snake(pos: int) -> int:
    global SNAKE_MAP

    if pos in SNAKE_MAP:
        print("Snake!!")
        return SNAKE_MAP[pos]
    else:
        return pos
    
def calc_position(pos: int) -> Position_info:
    if pos < 1:
        info = calc_position(1)
        info.x -= CELL_WIDTH
        return info
    
    pos -= 1 #Remap from 0 - 99
    row = pos // 10
    column = pos % 10
    is_odd = row % 2 == 1
    
    #Flip column on odd rows
    if is_odd:
        column = 9 - column
        rot = 180
    else:
        rot = 0

    return Position_info(START_X + (column * CELL_WIDTH), START_Y + (row * CELL_HEIGHT), rot)
    


#setting my screen
screen = turtle.Screen()
screen.bgpic("pics/Snakes-And-Ladders-Board.gif")
screen.setup(430,430)

#
p1 = turtle.Turtle()
p1.shape("turtle")
p1.color("black")
p1.speed(0)
p1.penup()
p1.setpos(calc_position(0).to_vec())
p1.speed(2)

p2 = turtle.Turtle()
p2.shape("turtle")
p2.color("violet")
p2.speed(0)
p2.penup()
p2.setpos(calc_position(0).to_vec())
p2.speed(2)

random.seed()

def won():
    tur = turtle.Turtle()
    tur.hideturtle()
    tur.pensize(8)
    tur.color("violet")
    tur.penup()
    tur.speed(0 )
    tur.goto(-200,200)
    tur.speed(0)
    tur.pendown()
    for _ in range(4):
        tur.forward(400)
        tur.right(90)
    tur.color("green")
    tur.fillcolor("green")
    tur.begin_fill()
    for _ in range(4):
        tur.forward(400)
        tur.right(90)
    tur.end_fill()

def rolling():
    n = random.randint(1, 6)
    print(f"Rolled: {n}")
    return n


def clicked():
    global ALLOW_TURN, TURN, SCOREP1, SCOREP2

    if not ALLOW_TURN:
        return
    else:
        ALLOW_TURN = False

    die = rolling()

    if TURN:
        player = p1
        score = SCOREP1
        name = "Player 1"
    else:
        player = p2
        score = SCOREP2
        name = "Player 2"

    new_score = score + die

    if new_score < END:
        # Move to new position
        for i in range(die + 1):
            info = calc_position(score + i)
            player.goto(info.to_vec())
            player.setheading(info.rot)
        
        # Check for ladders, then snakes
        new_score = check_snake(check_ladder(new_score))
        info = calc_position(new_score)
        player.goto(info.to_vec())
        player.setheading(info.rot)

        apply_score = True
    elif new_score > END:
        print(f"{name}, you can't exceed 100 :)")
        apply_score = False
    else:
        print(f"{name} won")
        player.goto(calc_position(100).to_vec())
        won()
        time.sleep(2)
        exit()

    if TURN:
        name = "Player 2"
        if apply_score:
            SCOREP1 = new_score
    else:
        name = "Player 1"
        if apply_score:
            SCOREP2 = new_score

    TURN = not TURN
    print(f"\n{name}, it's your turn")
    ALLOW_TURN = True

print("Player 1, it's your turn")
turtle.listen()
turtle.onkey(clicked,"space")
turtle.mainloop()