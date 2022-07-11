from turtle import Turtle

class Paddle(Turtle):
    #Defining the basic setup of the paddeles apperance
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
    #Method that enables upward movement of the paddles
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    #Method that enables downward movement of the paddles
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)