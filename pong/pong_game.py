import turtle
import os

window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # stop the window from updating drawings

# Paddle A
paddle_a = turtle.Turtle()  # creat a turtle object
# speed = 0 means no animation takes place. forward/back makes turtle jump
# and likewise left/right make the turtle turn instantly.
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # Set turtle's stretch factors
paddle_a.penup()  # Pull the pen up -- no drawing when moving.
paddle_a.goto(-350, 0)  # (0,0) is at the center of the screen

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
# add two attributes dx and dy to ball
ball.dx = 2
ball.dy = 2

# Scoring system
score_a = 0
score_b = 0
# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()  # Obtain the turtle's y coordinate
    y += 20  # add 20 pixels to y
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")  # press "w" key to move the paddle A up
window.onkeypress(paddle_a_down, "s")  # press "s" key to move the paddle A down
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # reverse the direction
        os.system("afplay bounce.wav&")  # aplay filename.mp3/wav etc.

    # bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # reverse the direction
        os.system("afplay bounce.wav&")

    # right border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # left border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if 350 > ball.xcor() > 340 and paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40:
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    if -350 < ball.xcor() < -340 and paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40:
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
