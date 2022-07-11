from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Set up Screen
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

#Using the paddle class to create the two pong paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
#Intializing the ping pong ball
ball = Ball()
scoreboard = Scoreboard()

#Using the turtle screen method to allow movement of the paddles with keyboard keys
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



#While loop used to update the screen after animations have been done
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #If statement that detects the  top and bottom walls to bounce the ball off of
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with the ball and paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    #Detect if right paddle has missed the ball
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    # Detect if leftt paddle has missed the ball
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()