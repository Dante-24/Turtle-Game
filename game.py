import turtle
import time
import random
import tkinter as tk
import pygame

pygame.init()

######################################
# New Game Window in Tkinter
######################################

mn = tk.Tk()
mn.title("New Game")
tk.Label(mn, text="Hope you will like the game.").grid(row=0, column=1)
tk.Label(mn, text="Press the arrow key according to the desired direction.").grid(row=1, column=1)
tk.Label(mn, text="Thank You!").grid(row=2, column=1)
tk.Label(mn).grid(row=3, column=2)

tk.Label(mn, text="Enter your name: ").grid(row=4)
en = tk.Entry(mn)
en.grid(row=4, column=1)

######################################
# Main Implementation of Code
######################################

def ray():
    pygame.mixer.music.load("sm3.mp3")
    pygame.mixer.music.play(-1, 0.0)

    name = en.get()
    sco = 0
    dist = 10

    wn = turtle.Screen()
    wn.reset()
    wn.title("Turtle Game by kratos_46")
    wn.bgcolor("green")
    sp = 1

    hd = turtle.Turtle()
    hd.shape("square")
    hd.pu()

    sc = turtle.Turtle()
    sc.shape("square")
    sc.color("white")
    sc.pu()
    sc.ht()
    sc.goto(0, 260)
    sc.write("Score: 0", align="center", font=("Courier", 24, "normal"))

    brd = turtle.Turtle()
    brd.ht()
    brd.pensize(4)
    brd.speed("fastest")
    brd.pu()
    brd.setpos(-250, 250)
    brd.pd()

    food = turtle.Turtle()
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0, 100)

    brd.begin_fill()
    for i in range(4):
        brd.fd(500)
        brd.rt(90)
    brd.color("blue")
    brd.end_fill()

######################################
# Boundary Checking and game rules
######################################

    def go_right():
        if hd.heading() != 180:
            hd.setheading(0)

    def go_up():
        if hd.heading() != 270:
            hd.setheading(90)

    def go_down():
        if hd.heading() != 90:
            hd.setheading(270)

    def go_left():
        if hd.heading() != 0:
            hd.setheading(180)

    wn.onkey(go_left, "Left")
    wn.onkey(go_right, "Right")
    wn.onkey(go_up, "Up")
    wn.onkey(go_down, "Down")
    wn.listen()

    while True:
        wn.update()
        hd.fd(dist)
        hd.speed(sp)

        if hd.xcor() > 245 or hd.xcor() < -245 or hd.ycor() > 245 or hd.ycor() < -245:
            pygame.mixer.music.stop()
            wn.reset()
            sc.ht()
            brd.ht()
            hd.ht()
            food.ht()
            hd.color("red")

######################################
# Scoreboard Display
######################################

            fp = open("Scores.txt", "a+")
            fp.write("\n" + name + " :" + str(int(sco)))
            fp.close()

            fp = open("Scores.txt", "r")
            ln = fp.readlines()
            dic = {}
            for xx in ln:
                a = xx.split(":")[0]
                b = xx.split(":")[1]
                dic.update({a: int(b)})
            l = sorted(dic.items(), key=lambda kv: (kv[1], kv[0]))[::-1]

            brd.pu()
            brd.speed("fastest")
            brd.goto(-150, 315)
            brd.pd()
            brd.begin_fill()
            for _ in range(2):
                brd.fd(300)
                brd.rt(90)
                brd.fd(600)
                brd.rt(90)
            brd.color("sky blue")
            brd.end_fill()
            brd.color("black")
            brd.pu()
            brd.goto(-150, 250)
            brd.pd()
            brd.fd(300)

            hd.pu()
            hd.goto(0, 200)
            hd.pd()

            for j in l[0:10]:
                if j[0].strip() == name and j[1] == int(sco):
                    hd.color("dark green")
                hd.write(j[0][0:3].upper() + " : " + str(j[1]), align="center", font=("Courier", 24, "normal"))
                hd.pu()
                hd.goto(0, hd.ycor() - 45)
                hd.pd()
                hd.color("red")
            hd.pu()
            hd.goto(0, 252)
            hd.pd()
            hd.color("Navy Blue")
            hd.write("High Scores", align="center", font=("MS Serif", 30, "underline"))

            turtle.done()

######################################
# Other Game Rules
######################################

        if hd.distance(food) < 20:
            x = random.randint(-245, 245)
            y = random.randint(-245, 245)
            food.ht()
            food.goto(x, y)
            food.st()
            sco += sp * 5
            dist += 2
            sp += 0.2
            sc.clear()
            sc.write("Score: %d" % (sco), align="center", font=("Courier", 24, "normal"))


b = tk.Button(mn, text="Click to Start", bg="green", font=("Courier", 10, "normal"), command=ray)
b.grid(row=5, column=2)
tk.mainloop()
