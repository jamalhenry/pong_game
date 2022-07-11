from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    #Method establishing movement of the ball
    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)
    #Method that changes the y cordinates and bounce off the walls
    def bounce_y(self):
        self.ymove *= -1
    # Method that changes the x cordinates and bounce off the walls
    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.9
    #Method that resets the ball once a user misses the ball
    def reset_ball(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
