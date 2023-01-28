import turtle
import time

delay = 0.1
# setup screen

wn = turtle.Screen()
wn.title("snake game by :sara")
wn.bgcolor("yellow")
wn.setup(width=600, height=600)
wn.tracer(0)


# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "up"

# funcions


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

        # main game loop
while True:
    wn.update()

    move()

    time.sleep(delay)

wn.mainloop()
