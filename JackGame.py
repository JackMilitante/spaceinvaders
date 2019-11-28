import turtle



#eater
eater = turtle.Turtle()
eater.color("yellow")
eater.shape("triangle")



def move_left():
    x = eater.xcor()
    x -= eaterspeed
    if x < -280:
        x = -280
    eater.setx(x)

def move_right():
    x = eater.xcor()
    x += eaterspeed
    if x > 280:
        x = 280
    eater.setx(x)