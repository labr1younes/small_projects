import turtle
        
class Player():
    
        # Player constructor
    def __init__(self, shape, color, width, lenght,position,player_speed ):
        self.plyr = turtle.Turtle()
        self.plyr.speed(0)
        self.plyr.shape(shape)
        self.plyr.color(color)
        self.plyr.shapesize(stretch_wid=width , stretch_len=lenght)
        self.plyr.penup()
        self.plyr.goto(position,0)
        self.player_speed = player_speed
        
        # player moving up  
    def move_up(self):
        y = self.plyr.ycor()
        y += self.player_speed
        self.plyr.sety(y)
        
        # player moving down
    def move_down(self):
        y = self.plyr.ycor()
        y -= self.player_speed
        self.plyr.sety(y)
        
class Ball():
    
        # Ball constructor
    def __init__(self,shape,color,ball_speed):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape(shape)
        self.ball.color(color)
        self.ball.dx = ball_speed
        self.ball.dy = ball_speed
        self.ball.penup()
        self.ball.goto(0,0)
        
        # ball moving automatically function
    def move(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)
        
        # checking the ball and the borders ofhe screen up and down
    def check_border_collision_up_down(self, width, height):
        if self.ball.ycor() > height / 2 - 10:
            self.ball.sety(height / 2 - 10)
            self.ball.dy *= -1
        elif self.ball.ycor() < -(height / 2 - 10):
            self.ball.sety(-(height / 2 - 10))
            self.ball.dy *= -1
            
        # checking the ball and the borders ofhe screen left and right ,to count the score
    def check_border_collision_left_right(self, width, height,left_score,right_score):
        if self.ball.xcor() > width / 2 - 10:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            left_score +=1
        elif self.ball.xcor() < -(width / 2 - 10):
            self.ball.goto(0, 0)
            self.ball.dx *= -1
            right_score +=1
        return left_score , right_score

class Game():
    
        # Game constructor
    def __init__(self ,width, height,title,bg_color,player_speed,ball_speed):
        self.width = width
        self.height = height
        self.window = turtle.Screen()
        self.window.title(title)
        self.window.bgcolor(bg_color)
        self.window.setup(width= self.width, height = self.height)
        self.window.tracer(0)

        self.player_x_pos = self.width / 2 - 25
        self.player_speed = player_speed
        self.ball_speed = ball_speed
        
        # score
        self.player_left_score = 0
        self.player_right_score = 0
        
        # initializing ball ,and players
        self.player_left = Player("square","white",5,1,-self.player_x_pos,self.player_speed)
        self.player_right = Player("square","white",5,1,self.player_x_pos,self.player_speed)
        self.ball = Ball("circle","white",self.ball_speed)
        
        # pen , we need it to write the score board
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.hideturtle()
        self.pen.goto(0,260)
        self.pen.write("Player(1): 0   Player(2): 0" , align="center",font=("Courier" , 20 ,"normal"))
        
        # updating the score on the screen
    def update_scores(self):
        self.pen.clear()
        self.pen.write("Player(1): {}   Player(2): {}".format(self.player_left_score, self.player_right_score),align="center", font=("Courier", 20, "normal"))
        
        # chekcing the ball and layers collision
    def ball_palyer_collision(self):
        t_bal = self.ball.ball
        r_ply = self.player_right.plyr
        l_ply = self.player_left.plyr
        
        #right player
        if ( t_bal.xcor() > (r_ply.xcor()-10) and t_bal.xcor() < r_ply.xcor())  and  ( t_bal.ycor() < r_ply.ycor() + 40 and t_bal.ycor() > r_ply.ycor() - 40):
            t_bal.setx(r_ply.xcor()-10)
            t_bal.dx *= -1
            
        #left player
        if (t_bal.xcor() > l_ply.xcor() and t_bal.xcor() < (l_ply.xcor() + 10)) and ( t_bal.ycor() < l_ply.ycor() + 40 and t_bal.ycor() > l_ply.ycor() - 40):
            t_bal.setx(l_ply.xcor() + 10)
            t_bal.dx *= -1
            
        # game start funciton 
    def start_game(self):
        
        # movement keys for the playrers 
        self.window.listen()
        self.window.onkeypress(self.player_left.move_up, "z")
        self.window.onkeypress(self.player_left.move_down, "s")
        self.window.onkeypress(self.player_right.move_up, "Up")
        self.window.onkeypress(self.player_right.move_down, "Down")
        
        # updating the screen score , ball, and pyalers positions
        while True:
            self.window.update()
            self.ball.move()
            self.ball.check_border_collision_up_down(self.width, self.height)
            self.player_left_score , self.player_right_score = self.ball.check_border_collision_left_right(self.width, self.height,self.player_left_score,self.player_right_score)
            self.ball_palyer_collision()
            self.update_scores()
            
# basic values
wi = 800
he = 600
player_speed = 35
ball_speed = 0.45
title = "Pong Game"
back_ground_color = "black"

# creating the game , and lunching it
game  = Game(wi,he,title,back_ground_color,player_speed,ball_speed)
game.start_game()
    
