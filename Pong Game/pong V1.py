import turtle

wi = 800
he = 600
wi2 = 800/2
he2 = 600 /2
movment = 35
ball_speed = 0.45
player_x_pos = wi2 - 25

window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width= wi, height = he)
window.tracer(0)

# score
score_plyr_1 = 0
score_plyr_2 = 0

#Player 1 
plyr_1 = turtle.Turtle()
plyr_1.speed(0)
plyr_1.shape("square")
plyr_1.color("white")
plyr_1.shapesize(stretch_wid=5 , stretch_len=1)
plyr_1.penup()
plyr_1.goto(-player_x_pos,0)

#Player 2  
plyr_2 = turtle.Turtle()
plyr_2.speed(0)
plyr_2.shape("square")
plyr_2.color("white")
plyr_2.shapesize(stretch_wid=5 , stretch_len=1)
plyr_2.penup()
plyr_2.goto(player_x_pos,0)

# Ball   
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
#ball.shapesize(stretch_wid=5 , stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx = ball_speed
ball.dy = ball_speed

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player(1): 0   Player(2): 0" , align="center",font=("Courier" , 20 ,"normal"))

# functions 
def plyr_1_up():
    y = plyr_1.ycor()
    y += movment
    plyr_1.sety(y)

def plyr_1_dwn():
    y = plyr_1.ycor()
    y -= movment
    plyr_1.sety(y)

def plyr_2_up(): 
    y = plyr_2.ycor()
    y += movment
    plyr_2.sety(y)

def plyr_2_dwn(): 
    y = plyr_2.ycor()
    y -= movment
    plyr_2.sety(y)
    
# keyboard binging
window.listen()
window.onkeypress(plyr_1_up,"z")
window.onkeypress(plyr_1_dwn,"s")

window.onkeypress(plyr_2_up,"Up")
window.onkeypress(plyr_2_dwn,"Down")
# main Game 
while True:
    window.update()

    # ball movment 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border cheking up and down 
    if ball.ycor() > (he2 -10) :
        ball.sety(he2 -10)
        ball.dy *= -1

    if ball.ycor() < -(he2 -10) :
        ball.sety(-(he2 -10))
        ball.dy *= -1
        
    # border cheking left and right 
    if ball.xcor() > (wi2 -10):
        ball.goto(0,0)
        ball.dx *= -1
        score_plyr_1 +=1
        pen.clear()
        pen.write("Player(1): {}   Player(2): {}".format(score_plyr_1,score_plyr_2) , align="center",font=("Courier" , 20 ,"normal"))

    if ball.xcor() < -(wi2 -10):
        ball.goto(0,0)
        ball.dx *= -1
        score_plyr_2 +=1
        pen.clear()
        pen.write("Player(1): {}   Player(2): {}".format(score_plyr_1,score_plyr_2) , align="center",font=("Courier" , 20 ,"normal"))

    # Player and ball collision
    if ( ball.xcor() > (player_x_pos-10) and ball.xcor() < player_x_pos)  and  ( ball.ycor() < plyr_2.ycor() + 40 and ball.ycor() > plyr_2.ycor() - 40):
        ball.setx((player_x_pos-10))
        ball.dx *= -1        

    if ( ball.xcor() < -(player_x_pos-10) and ball.xcor() > -player_x_pos ) and  ( ball.ycor() < plyr_1.ycor() + 40 and ball.ycor() > plyr_1.ycor() - 40):
        ball.setx(-(player_x_pos-10))
        ball.dx *= -1
    
