import turtle
import keyboard

onecorchange = .20
ballchange = .3

p1score = 0
p2score = 0

window = turtle.Screen()
window.title("RockSoccer")
window.bgcolor("green")
window.setup(width=600, height=400)
window.tracer(0)

score = turtle.Turtle()
score.hideturtle()

directions = turtle.Turtle()
directions.speed(0)
directions.color("black")
directions.penup()
directions.hideturtle()
directions.goto(0, 10)
directions.write("WASD for player 1 and arrow keys for player 2", align="center", font=("Courtier", 14, "normal"))
directions2 = turtle.Turtle()
directions2.speed(0)
directions2.color("black")
directions2.penup()
directions2.hideturtle()
directions2.goto(0, -30)
directions2.write("Press SPACE if ball gets stuff", align="center", font=("Courtier", 14, "normal"))

border = turtle.Turtle()
border.speed(0)
border.shape("square")
border.color("red")
border.shapesize(stretch_wid=10, stretch_len=1)
border.penup()
border.goto(-300, 0)

border2 = turtle.Turtle()
border2.speed(0)
border2.shape("square")
border2.color("blue")
border2.shapesize(stretch_wid=10, stretch_len=1)
border2.penup()
border2.goto(293, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("grey")
ball.shapesize(stretch_wid=0.75, stretch_len=0.75)
ball.penup()
ball.goto(0, 0)

s1 = turtle.Turtle()
s1.speed(0)
s1.shape("square")
s1.color("red")
s1.shapesize(stretch_wid=0.75, stretch_len=0.05)
s1.penup()
s1.goto(0, 0)
s1.hideturtle()

s2 = turtle.Turtle()
s2.speed(0)
s2.shape("square")
s2.color("blue")
s2.shapesize(stretch_wid=0.05, stretch_len=0.75)
s2.penup()
s2.goto(0, 0)
s2.hideturtle()

s3 = turtle.Turtle()
s3.speed(0)
s3.shape("square")
s3.color("yellow")
s3.shapesize(stretch_wid=0.75, stretch_len=0.05)
s3.penup()
s3.goto(0, 0)
s3.hideturtle()

s4 = turtle.Turtle()
s4.speed(0)
s4.shape("square")
s4.color("purple")
s4.shapesize(stretch_wid=0.05, stretch_len=0.75)
s4.penup()
s4.goto(0, 0)
s4.hideturtle()

p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("red")
p1.shapesize(stretch_wid=2, stretch_len=2)
p1.penup()
p1.goto(-250, 0)

p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("blue")
p2.shapesize(stretch_wid=2, stretch_len=2)
p2.penup()
p2.goto(250, 0)

go = True
while go:
    if keyboard.is_pressed("w"):
        p1.sety(p1.ycor() + onecorchange)
    if keyboard.is_pressed("s"):
        p1.sety(p1.ycor() - onecorchange)
    if keyboard.is_pressed("a"):
        p1.setx(p1.xcor() - onecorchange)
    if keyboard.is_pressed("d"):
        p1.setx(p1.xcor() + onecorchange)
        directions.clear()
        directions2.clear()

    if keyboard.is_pressed("up"):
        p2.sety(p2.ycor() + onecorchange)
    if keyboard.is_pressed("down"):
        p2.sety(p2.ycor() - onecorchange)
    if keyboard.is_pressed("left"):
        p2.setx(p2.xcor() - onecorchange)
        directions.clear()
        directions2.clear()
    if keyboard.is_pressed("right"):
        p2.setx(p2.xcor() + onecorchange)

    if p1.xcor() >= 275:
        p1.setx(275)
    if p1.xcor() <= -275:
        p1.setx(-275)
    if p1.ycor() >= 175:
        p1.sety(175)
    if p1.ycor() <= -175:
        p1.sety(-175)

    if p2.xcor() >= 275:
        p2.setx(275)
    if p2.xcor() <= -275:
        p2.setx(-275)
    if p2.ycor() >= 175:
        p2.sety(175)
    if p2.ycor() <= -175:
        p2.sety(-175)

    if ball.xcor() >= 290:
        ball.setx(290)
    if ball.xcor() <= -290:
        ball.setx(-290)
    if ball.ycor() >= 190:
        ball.sety(190)
    if ball.ycor() <= -190:
        ball.sety(-190)

    if abs(p1.xcor() - s1.xcor()) < 20 and abs(p1.ycor() - s1.ycor()) < 20:
        ball.setx(ball.xcor() + ballchange)
    if abs(p1.xcor() - s2.xcor()) < 20 and abs(p1.ycor() - s2.ycor()) < 20:
        ball.sety(ball.ycor() - ballchange)
    if abs(p1.xcor() - s3.xcor()) < 20 and abs(p1.ycor() - s3.ycor()) < 20:
        ball.setx(ball.xcor() - ballchange)
    if abs(p1.xcor() - s4.xcor()) < 20 and abs(p1.ycor() - s4.ycor()) < 20:
        ball.sety(ball.ycor() + ballchange)

    if abs(p2.xcor() - s1.xcor()) < 20 and abs(p2.ycor() - s1.ycor()) < 20:
        ball.setx(ball.xcor() + ballchange)
    if abs(p2.xcor() - s2.xcor()) < 20 and abs(p2.ycor() - s2.ycor()) < 20:
        ball.sety(ball.ycor() - ballchange)
    if abs(p2.xcor() - s3.xcor()) < 20 and abs(p2.ycor() - s3.ycor()) < 20:
        ball.setx(ball.xcor() - ballchange)
    if abs(p2.xcor() - s4.xcor()) < 20 and abs(p2.ycor() - s4.ycor()) < 20:
        ball.sety(ball.ycor() + ballchange)

    if abs(border.xcor() - ball.xcor()) < 17 and abs(border.ycor() - ball.ycor()) < 100:
        ball.goto(0, 0)
        p1.goto(-250, 0)
        p2.goto(250, 0)
        p1score += 1
        score.undo()
        score.speed(0)
        score.color("black")
        score.hideturtle()
        score.penup()
        score.goto(0, 175)
        score.write(f"P1:{p1score}  P2:{p2score}", align="center", font=("Courtier", 14, "normal"))
    if abs(border2.xcor() - ball.xcor()) < 17 and abs(border2.ycor() - ball.ycor()) < 100:
        ball.goto(0, 0)
        p1.goto(-250, 0)
        p2.goto(250, 0)
        p2score += 1
        score.undo()
        score.speed(0)
        score.color("black")
        score.hideturtle()
        score.penup()
        score.goto(0, 175)
        score.write(f"P1:{p1score}  P2:{p2score}", align="center", font=("Courtier", 14, "normal"))

    if keyboard.is_pressed("space"):
        ball.goto(0, 0)

    s1.setx(ball.xcor() - 9)
    s1.sety(ball.ycor())
    s2.setx(ball.xcor())
    s2.sety(ball.ycor() + 9)
    s3.setx(ball.xcor() + 9)
    s3.sety(ball.ycor())
    s4.setx(ball.xcor())
    s4.sety(ball.ycor() - 9)
    window.update()
