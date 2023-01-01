import turtle
import time
import random
import subprocess
import tkinter as tk
import os
import sys
from threading import Thread

score = 0
high_score = 0
speed = 0.2
# to store new snake bodys
segment_snake1 = []
segment_snake2 = []

# get current path directory
current_path = os.path.abspath(sys.path[0])

# Create turtle window screen
turtle_screen = turtle.Screen()
turtle_screen.setup(800, 800)
turtle_screen.title("Snake")

# no updates to screen
turtle_screen.tracer(0, 0)
# play sound effect in screen
def play_music():
    audio_file = f"{current_path}" + "/sounds/music_theme.mp3"
    subprocess.call(["afplay", audio_file])
#     winsound.PlaySound("sounds/music_theme.mp3", winsound.SND_ASYNC)


def play_crashsound():
    audio_file = f"{current_path}" + "/sounds/crash.mp3"
    subprocess.call(["afplay", audio_file])


def play_point_gain():
    audio_file = f"{current_path}" + "/sounds/point_gain.wav"
    subprocess.call(["afplay", audio_file])


def play_super_point_gain():
    audio_file = f"{current_path}" + "/sounds/superpoint_gain.mp3"
    subprocess.call(["afplay", audio_file])


def play_bonus_point_gain():
    audio_file = f"{current_path}" + "/sounds/bonuspoint_gain.mp3"
    subprocess.call(["afplay", audio_file])

# sound trackers
music_state = False
crash_state = False
pointgain_state = False

#initialise timer
time_left = 60
ending_time = 0

timer = turtle.Turtle()
timer.speed(0)
timer.shape("square")
timer.color("white")
timer.penup()
timer.hideturtle()
timer.goto(0, 350)
game_state = 0

# Create snake
snake1 = turtle.Turtle()
snake1.shape("square")
snake1.color("blue")
snake1.speed(0)
snake1.penup()
snake1.goto(100, 100)
snake1.direction = "stop"
snake1.ht()
snake2 = turtle.Turtle()
snake2.shape("square")
snake2.color("red")
snake2.speed(0)
snake2.penup()
snake2.goto(-100, -100)
snake2.direction = "stop"
snake2.ht()
snake_list = [snake1, snake2]

# Create snake foods
foods = []
food1 = turtle.Turtle()
food1.speed(0)
food1.shape("square")
food1.color("green")
food1.penup()
food1.shapesize(0.5, 0.5)
food1.goto(0, 0)
foods.append(food1)
food1.ht()

# Declare variables to check stage of added food
foodadded_state = 0
superfoodadded_state = 0
bonusfood_isadded_state = 0

# variables to modify for each stage
# number of food to spawn when touch superfood
xfood_number = 0
# starting time of superfood spawning
superfood_checkpoint = 40
# timer of superfood expiry
superfood_timer = 0

# Superfood Lists
sfoods_list = []
xfoods_list = []
bfood_list = []

# initialise pen to update scores. Can use pen to show screen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

#startscreen
#Title screen
start_pen = turtle.Turtle()
start_pen.speed(0)
start_pen.penup()
start_pen.color("black")
start_pen.hideturtle()
start_pen.goto(0, 250)
start_pen.write("PYTHONS", align="center", font=("Courier", 40, "normal"))
start_pen.goto(0, -25)
start_pen.write("Ask a friend to join in the fun!", align="center", font=("Courier", 20, "normal"))


def start_game():
    try:
        food_specimen.ht()
        xfood_specimen.ht()
        sfood_specimen.ht()
        bfood_specimen.ht()
        turtle_screen.update()
    except:
        pass
    try:
        button1.destroy()
    except:
        pass
    try:
        button2.destroy()
    except:
        pass
    try:
        button3.destroy()
    except:
        pass
    try:
        button4.destroy()
    except:
        pass
    canvas.delete("snake1")
    canvas.delete("snake2")
    canvas.delete("snake3")
    canvas.delete("snake4")
    #initialise game here
    start_pen.clear()
    global game_state
    game_state = 1
    food1.st()
    snake1.st()
    snake2.st()
    pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))
    timer.write(f"Time Left: {time_left}s", align="center", font=("Courier", 24, "normal"))
    turtle_screen.bgcolor("black")

def next_frame():
    try:
        canvas.delete("up_arrow")
        canvas.delete("down_arrow")
        canvas.delete("left_arrow")
        canvas.delete("right_arrow")
    except:
        pass
    try:
        button3.destroy()
    except:
        pass
    start_pen.clear()
    start_pen.speed(0)
    start_pen.penup()
    start_pen.color("black")
    start_pen.hideturtle()
    start_pen.goto(0, 225)
    start_pen.write("POWER UPS:)", align="center", font=("Courier", 40, "normal"))
    start_pen.color("green")
    global xfood_specimen
    xfood_specimen = turtle.Turtle()
    xfood_specimen.speed(0)
    xfood_specimen.shape("square")
    xfood_specimen.color("purple")
    xfood_specimen.penup()
    xfood_specimen.shapesize(0.5, 0.5)
    xfood_specimen.goto(-325, 135)
    start_pen.goto(-225, 125)
    start_pen.write(": 10 points", align="center", font=("Courier", 20, "normal"))
    global food_specimen
    food_specimen = turtle.Turtle()
    food_specimen.penup()
    food_specimen.speed(0)
    food_specimen.shape("square")
    food_specimen.color("green")
    food_specimen.shapesize(0.5, 0.5)
    food_specimen.goto(-325, 50)
    start_pen.goto(-19, 40)
    start_pen.write(": 20 points + snake grows longer and faster", align="center", font=("Courier", 20, "normal"))
    global sfood_specimen
    sfood_specimen = turtle.Turtle()
    sfood_specimen.penup()
    sfood_specimen.speed(0)
    sfood_specimen.shape("circle")
    sfood_specimen.color("yellow")
    sfood_specimen.shapesize(1, 1)
    sfood_specimen.goto(-325, -35)
    start_pen.goto(-70, -45)
    start_pen.write(": 50 points + spawns purple food", align="center", font=("Courier", 20, "normal"))
    global bfood_specimen
    bfood_specimen = turtle.Turtle()
    bfood_specimen.penup()
    bfood_specimen.speed(0)
    bfood_specimen.shape("circle")
    bfood_specimen.color("chartreuse")
    bfood_specimen.shapesize(1, 1)
    bfood_specimen.goto(-325, -120)
    start_pen.goto(35, -130)
    start_pen.write(": 200 points + spawns only in the last 10 seconds!", align="center", font=("Courier", 20, "normal"))
    global button4
    button4 = tk.Button(canvas.master, bg='black', fg='green', text="I'm ready!", command=start_game)
    canvas.create_window(0, 240, window=button4)

def press():
    canvas.delete("snake1")
    canvas.delete("snake2")
    canvas.delete("snake3")
    canvas.delete("snake4")
    button1.destroy()
    button2.destroy()
    start_pen.clear()
    start_pen.speed(0)
    start_pen.penup()
    start_pen.color("black")
    start_pen.hideturtle()
    start_pen.goto(0, 225)
    start_pen.write("HOW TO PLAY", align="center", font=("Courier", 40, "normal"))
    start_pen.goto(0, 175)
    start_pen.write("Controls:", align="center", font=("Courier", 20, "normal"))
    start_pen.goto(-240, 125)
    start_pen.color("green")
    start_pen.write("Player 1: ", align="center", font=("Courier", 20, "normal"))
    start_pen.goto(150, 92)
    start_pen.color("green")
    start_pen.write("D: move right", align="center", font=("Courier", 20, "normal"))
    start_pen.goto(144, 62)
    start_pen.write("A: move left", align="center", font=("Courier", 20, "normal"))
    start_pen.goto(132, 32)
    start_pen.write("W: move up", align="center", font=("Courier", 20, "normal"))
    start_pen.goto(144, 2)
    start_pen.write("S: move down", align="center", font=("Courier", 20, "normal"))
    start_pen.goto(-240, -75)
    start_pen.color("red")
    start_pen.write("Player 2: ", align="center", font=("Courier", 20, "normal"))
    canvas.down_arrow_button = tk.PhotoImage(file=f"{current_path}" + '/images/downarrow.png')
    canvas.left_arrow_button = tk.PhotoImage(file=f"{current_path}" + '/images/leftarrow.png')
    canvas.right_arrow_button = tk.PhotoImage(file=f"{current_path}" + '/images/rightarrow.png')
    canvas.up_arrow_button = tk.PhotoImage(file=f"{current_path}" + '/images/uparrow.png')
    canvas.create_image(80, 100, image=canvas.right_arrow_button, tags="right_arrow")
    start_pen.goto(125, -110)
    start_pen.write(": move right ", align="left", font=("Courier", 20, "normal"))
    canvas.create_image(80, 150, image=canvas.left_arrow_button, tags="left_arrow")
    start_pen.goto(125, -160)
    start_pen.write(": move left ", align="left", font=("Courier", 20, "normal"))
    canvas.create_image(80, 200, image=canvas.up_arrow_button, tags="up_arrow")
    start_pen.goto(125, -210)
    start_pen.write(": move up ", align="left", font=("Courier", 20, "normal"))
    canvas.create_image(80, 250, image=canvas.down_arrow_button, tags="down_arrow")
    start_pen.goto(125, -260)
    start_pen.write(": move down ", align="left", font=("Courier", 20, "normal"))
    global button3
    button3 = tk.Button(canvas.master, bg='black', fg='green', text="Next!", command=next_frame)
    canvas.create_window(0, 240, window=button3)
    button3.place(x=350, y=720)

#startscreen
canvas = turtle_screen.getcanvas()
canvas.snake1 = tk.PhotoImage(file=f"{current_path}" + '/images/snake1.png')
canvas.snake2 = tk.PhotoImage(file=f"{current_path}" + '/images/snake2.png')
canvas.snake3 = tk.PhotoImage(file=f"{current_path}" + '/images/snake3.png')
canvas.snake4 = tk.PhotoImage(file=f"{current_path}" + '/images/snake4.png')
canvas.create_image(-300, 300, image=canvas.snake1, tags="snake1")
canvas.create_image(-300, -300, image=canvas.snake2, tags="snake2")
canvas.create_image(300, 300, image=canvas.snake3, tags="snake3")
canvas.create_image(300, -300, image=canvas.snake4, tags="snake4")
button1 = tk.Button(canvas.master, bg='black', fg='black', text="Learn how to play", command=press)
canvas.create_window(100, 100, window=button1)
button2 = tk.Button(canvas.master, bg='black', fg='black', text="I'm ready!", command=start_game)
canvas.create_window(-100, 100, window=button2)

#endscreen
endscreen = turtle.Turtle()
lf = endscreen.left
bd = endscreen.backward
sh = endscreen.setheading
endscreen.speed(10)
endscreen.ht()

def g(x,y):
    endscreen.pu()
    endscreen.goto(x,y)
    endscreen.pd()
    endscreen.width(10)
    endscreen.pencolor('DarkOrchid1')
    endscreen.left(180)
    endscreen.fd(100)
    endscreen.left(90)
    endscreen.fd(100)
    endscreen.left(90)
    endscreen.fd(100)
    endscreen.left(90)
    endscreen.fd(50)
    endscreen.left(90)
    endscreen.fd(50)
    endscreen.pu()
    endscreen.setheading(0)

def a(x,y):
    endscreen.width(10)
    endscreen.pu()
    endscreen.goto(x,y)
    endscreen.pencolor('red')
    endscreen.pd()
    endscreen.left(90)
    endscreen.fd(100)
    endscreen.right(90)
    endscreen.fd(100)
    endscreen.right(90)
    endscreen.fd(100)
    endscreen.pu()
    endscreen.backward(50)
    endscreen.right(90)
    endscreen.fd(100)
    endscreen.pd()
    endscreen.backward(100)
    endscreen.setheading(0)

def m(x,y):
    endscreen.width(10)
    endscreen.pu()
    endscreen.goto(x,y)
    endscreen.pencolor('DarkOrchid1')
    endscreen.pd()
    endscreen.left(90)
    endscreen.fd(100)
    endscreen.right(90)
    endscreen.fd(50)
    endscreen.right(90)
    endscreen.fd(100)
    endscreen.backward(100)
    endscreen.left(90)
    endscreen.fd(50)
    endscreen.right(90)
    endscreen.fd(100)
    endscreen.setheading(0)

def e(x,y):
    endscreen.pu()
    endscreen.goto(x,y)
    endscreen.pd()
    endscreen.width(10)
    endscreen.pencolor('red')
    endscreen.left(180)
    endscreen.fd(100)
    endscreen.left(90)
    endscreen.fd(50)
    endscreen.left(90)
    endscreen.fd(100)
    endscreen.pu()
    endscreen.backward(100)
    endscreen.pd()
    endscreen.right(90)
    endscreen.fd(50)
    endscreen.left(90)
    endscreen.fd(100)
    endscreen.pu()
    endscreen.setheading(0)

def o(x,y):
    endscreen.width(10)
    endscreen.pu()
    endscreen.goto(x,y)
    endscreen.pencolor('red')
    endscreen.pd()
    endscreen.left(90)
    endscreen.fd(100)
    endscreen.right(90)
    endscreen.fd(100)
    endscreen.right(90)
    endscreen.fd(100)
    endscreen.right(90)
    endscreen.fd(100)
    endscreen.pu()
    endscreen.setheading(0)

def v(x,y):
    endscreen.width(10)
    endscreen.pu()
    endscreen.goto(x,y)
    endscreen.pencolor('DarkOrchid1')
    endscreen.pd()
    endscreen.right(90-26.56505118)
    endscreen.fd(111.8)
    endscreen.left(2*(90-26.56505118))
    endscreen.fd(111.8)
    endscreen.pu()
    endscreen.setheading(0)

def r(x,y):
    endscreen.width(10)
    endscreen.pu()
    endscreen.goto(x,y)
    endscreen.pencolor('DarkOrchid1')
    endscreen.pd()
    endscreen.left(90)
    endscreen.fd(100)
    endscreen.right(90)
    endscreen.fd(100)
    endscreen.right(90)
    endscreen.fd(50)
    endscreen.right(90)
    endscreen.fd(100)
    endscreen.left(180-26.56505118)
    endscreen.fd(111.8)
    endscreen.setheading(0)

def move(snake):
    """Move snake based on the direction attribute of snake"""
    if snake.direction == 'up':
        snake.sety(snake.ycor() + 20)
    elif snake.direction == 'down':
        snake.sety(snake.ycor() - 20)
    elif snake.direction == 'right':
        snake.setx(snake.xcor() + 20)
    elif snake.direction == 'left':
        snake.setx(snake.xcor() - 20)

"""Change snake direction if the direction is not the opposite"""
def go_left_snake1():
    if snake1.direction != "right":
        snake1.direction = "left"

def go_right_snake1():
    if snake1.direction != "left":
        snake1.direction = "right"

def go_up_snake1():
    if snake1.direction != "down":
        snake1.direction = "up"

def go_down_snake1():
    if snake1.direction != "up":
        snake1.direction = "down"

def go_left_snake2():
    if snake2.direction != "right":
        snake2.direction = "left"

def go_right_snake2():
    if snake2.direction != "left":
        snake2.direction = "right"

def go_up_snake2():
    if snake2.direction != "down":
        snake2.direction = "up"

def go_down_snake2():
    if snake2.direction != "up":
        snake2.direction = "down"

# Bind keys to change in direction
turtle_screen.listen()
turtle_screen.onkey(go_left_snake1, "Left")
turtle_screen.onkey(go_right_snake1, "Right")
turtle_screen.onkey(go_down_snake1, "Down")
turtle_screen.onkey(go_up_snake1, "Up")
turtle_screen.onkey(go_left_snake2, "a")
turtle_screen.onkey(go_right_snake2, "d")
turtle_screen.onkey(go_down_snake2, "s")
turtle_screen.onkey(go_up_snake2, "w")

while True:
    """Main game loop"""

    turtle_screen.update()
    time.sleep(speed)
    if music_state == False:
        music_thread = Thread(target=play_music)
        music_thread.start()
        music_state = True
    if game_state == 1 or game_state == 2:
        # add additional foods at intervals
        if (time_left < 40 and foodadded_state == 0):
            foodadded_state += 1
            food2 = turtle.Turtle()
            food2.speed(0)
            food2.shape("square")
            food2.color("green")
            food2.penup()
            food2.shapesize(0.5, 0.5)
            food2.goto(random.randint(-390, 390), random.randint(-390, 390))
            foods.append(food2)

        if (time_left < 20 and foodadded_state == 1):
            foodadded_state += 1
            food3 = turtle.Turtle()
            food3.speed(0)
            food3.shape("square")
            food3.color("green")
            food3.penup()
            food3.shapesize(0.5, 0.5)
            food3.goto(random.randint(-390, 390), random.randint(-390, 390))
            foods.append(food3)

        if (time_left < 10 and foodadded_state == 2):
            foodadded_state += 1
            food4 = turtle.Turtle()
            food4.speed(0)
            food4.shape("square")
            food4.color("green")
            food4.penup()
            food4.shapesize(0.5, 0.5)
            food4.goto(random.randint(-390, 390), random.randint(-390, 390))
            foods.append(food4)
        # add super foods based on timer
        if time_left <= superfood_checkpoint and time_left >= 9:
            # spawn at 40, 20 , 10
            if superfoodadded_state < 3:
                superfood_checkpoint -= 20/(superfoodadded_state + 1)
            xfood_number += 5
            sfoods_list.append(turtle.Turtle())
            sfoods_list[0].speed(0)
            sfoods_list[0].shape("circle")
            sfoods_list[0].color("yellow")
            sfoods_list[0].penup()
            sfoods_list[0].shapesize(1, 1)
            sfoods_list[0].goto(random.randint(-390, 390), random.randint(-390, 390))
            superfood_timer = 10
            superfoodadded_state += 1
        if superfood_timer > 0:
            superfood_timer -= speed
        elif sfoods_list:
            sfoods_list[0].ht()
            sfoods_list.clear()
            superfood_timer = 0

        if (time_left < 10 and bonusfood_isadded_state == 0):
            bonusfood_isadded_state += 1
            bfood1 = turtle.Turtle()
            bfood1.speed(0)
            bfood1.shape("circle")
            bfood1.color("chartreuse")
            bfood1.penup()
            bfood1.shapesize(1, 1)
            bfood1.goto(random.randint(-390, 390), random.randint(-390, 390))
            bfood_list.append(bfood1)

        if (time_left < 5 and bonusfood_isadded_state == 1):
            bonusfood_isadded_state +=1
            bfood2 = turtle.Turtle()
            bfood2.speed(0)
            bfood2.shape("circle")
            bfood2.color("chartreuse")
            bfood2.penup()
            bfood2.shapesize(1, 1)
            bfood2.goto(random.randint(-390, 390), random.randint(-390, 390))
            bfood_list.append(bfood2)

        # relocates food to new position if snake touches food
        for food in foods:
            if snake1.distance(food) < 15:
                thread = Thread(target=play_point_gain)
                thread.start()
                # winsound.PlaySound('sounds/point_gain.wav', winsound.SND_ASYNC)
                score += 20
                speed = speed * 9 / 10
                food.goto(random.randint(-390, 390), random.randint(-390, 390))
                # Adds length to snake body after touching food
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("blue")
                new_segment.penup()
                segment_snake1.append(new_segment)
            if snake2.distance(food) < 15:
                thread = Thread(target=play_point_gain)
                thread.start()
                # winsound.PlaySound('sounds/point_gain.wav', winsound.SND_ASYNC)
                score += 20
                speed = speed * 9 / 10
                food.goto(random.randint(-390, 390), random.randint(-390, 390))
                # Adds length to snake body after touching food
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("red")
                new_segment.penup()
                segment_snake2.append(new_segment)
        if sfoods_list:
            if snake1.distance(sfoods_list[0]) < 15:
                thread = Thread(target=play_super_point_gain)
                thread.start()
                # winsound.PlaySound('sounds/point_gain.wav', winsound.SND_ASYNC)
                score += 50
                # Adds length to snake body after touching food
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("blue")
                new_segment.penup()
                segment_snake1.append(new_segment)
                sfoods_list[0].ht()
                sfoods_list.clear()
                for i in range(xfood_number):
                    xfoods_list.append(turtle.Turtle())
                for food in xfoods_list:
                    food.speed(0)
                    food.shape("square")
                    food.color("purple")
                    food.penup()
                    food.shapesize(0.5, 0.5)
                    food.goto(random.randint(-390, 390), random.randint(-390, 390))
            elif snake2.distance(sfoods_list[0]) < 15:
                thread = Thread(target=play_super_point_gain)
                thread.start()
                # winsound.PlaySound('sounds/point_gain.wav', winsound.SND_ASYNC)
                score += 50
                speed = speed * 9 / 10
                sfoods_list[0].goto(random.randint(-390, 390), random.randint(-390, 390))
                # Adds length to snake body after touching food
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("red")
                new_segment.penup()
                segment_snake2.append(new_segment)
                sfoods_list[0].ht()
                sfoods_list.clear()
                for i in range(xfood_number):
                    xfoods_list.append(turtle.Turtle())
                for food in xfoods_list:
                    food.speed(0)
                    food.shape("square")
                    food.color("purple")
                    food.penup()
                    food.shapesize(0.5, 0.5)
                    food.goto(random.randint(-390, 390), random.randint(-390, 390))

        for food in xfoods_list:
            if snake1.distance(food) < 15:
                thread = Thread(target=play_point_gain)
                thread.start()
                score += 10
                # Adds length to snake body after touching food
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("blue")
                new_segment.penup()
                segment_snake1.append(new_segment)
                xfoods_list.remove(food)
                food.ht()
            if snake2.distance(food) < 15:
                thread = Thread(target=play_point_gain)
                thread.start()
                # winsound.PlaySound('sounds/point_gain.wav', winsound.SND_ASYNC)
                score += 10
                # Adds length to snake body after touching food
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("red")
                new_segment.penup()
                segment_snake2.append(new_segment)
                xfoods_list.remove(food)
                food.ht()
        for bfood in bfood_list:
            if snake1.distance(bfood) < 15:
                thread = Thread(target=play_bonus_point_gain)
                thread.start()
                score += 200
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("chartreuse")
                new_segment.penup()
                segment_snake1.append(new_segment)
                bfood.ht()
            elif snake2.distance(bfood) < 15:
                thread = Thread(target=play_bonus_point_gain)
                thread.start()
                score += 200
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("chartreuse")
                new_segment.penup()
                segment_snake2.append(new_segment)
                bfood.ht()
        # move the segments of both snakes accordingly
        for i in range(len(segment_snake1) - 1, 0, -1):
            x = segment_snake1[i - 1].xcor()
            y = segment_snake1[i - 1].ycor()
            segment_snake1[i].goto(x, y)
        for i in range(len(segment_snake2) - 1, 0, -1):
            x = segment_snake2[i - 1].xcor()
            y = segment_snake2[i - 1].ycor()
            segment_snake2[i].goto(x, y)
        # First segment will go to the snake object coordinates instead
        if segment_snake1:
            segment_snake1[0].goto(snake1.xcor(), snake1.ycor())
        if segment_snake2:
            segment_snake2[0].goto(snake2.xcor(), snake2.ycor())
        for snake in snake_list:
            move(snake)
            # Do checks here for all collision and reset (game is not over)
            """collision with walls"""
            if snake.xcor() > 390 or snake.xcor() < -390 or snake.ycor() > 390 or snake.ycor() < -390:
                # winsound.PlaySound('sounds/crash.wav', winsound.SND_ASYNC)
                thread = Thread(target=play_crashsound)
                thread.start()
                time.sleep(2)
                speed = 0.2
                if snake == snake1:
                    for segment in segment_snake1:
                        segment.ht()
                    segment_snake1.clear()
                elif snake == snake2:
                    for segment in segment_snake2:
                        segment.ht()
                    segment_snake2.clear()
                snake.direction = "stop"
                snake.goto(0, 0)
        # collision between snakes head
        if snake1.distance(snake2) < 15:
            thread = Thread(target=play_crashsound)
            thread.start()
            time.sleep(2)
            speed = 0.2
            # winsound.PlaySound('sounds/crash.wav', winsound.SND_ASYNC)
            for segment in segment_snake1:
                segment.ht()
            for segment in segment_snake2:
                segment.ht()
            segment_snake1.clear()
            segment_snake2.clear()
            for snake in snake_list:
                snake.direction = "stop"
            snake1.goto(100, 0)
            snake2.goto(-100, 0)
        # collision between snake bodys
        for segment in segment_snake1:
            # check if collide with other snake
            if snake2.distance(segment) < 15:
                thread = Thread(target=play_crashsound)
                thread.start()
                time.sleep(2)
                speed = 0.2
                # winsound.PlaySound('sounds/crash.wav', winsound.SND_ASYNC)
                for segment in segment_snake2:
                    segment.ht()
                segment_snake2.clear()
                snake2.direction = "stop"
                snake2.goto(0, 0)
            # check if collide with own snake body
            if snake1.distance(segment) < 15:
                thread = Thread(target=play_crashsound)
                thread.start()
                time.sleep(2)
                speed = 0.2
                # winsound.PlaySound('sounds/crash.wav', winsound.SND_ASYNC)
                for segment in segment_snake1:
                    segment.ht()
                segment_snake1.clear()
                snake1.direction = "stop"
                snake1.goto(0, 0)
        for segment in segment_snake2:
            # check if collide with other snake
            if snake1.distance(segment) < 15:
                thread = Thread(target=play_crashsound)
                thread.start()
                time.sleep(2)
                speed = 0.2
                # winsound.PlaySound('sounds/crash.wav', winsound.SND_ASYNC)
                for segment in segment_snake1:
                    segment.ht()
                segment_snake1.clear()
                snake1.direction = "stop"
                snake1.goto(0, 0)
            # check if collide with own snake body
            if snake2.distance(segment) < 15:
                thread = Thread(target=play_crashsound)
                thread.start()
                time.sleep(2)
                speed = 0.2
                # winsound.PlaySound('sounds/crash.wav', winsound.SND_ASYNC)
                for segment in segment_snake1:
                    segment.ht()
                segment_snake2.clear()
                snake2.direction = "stop"
                snake2.goto(0, 0)

        #countdown
        if snake1.xcor() != 100 or snake1.ycor() != 100:
            game_state = 2
        elif snake2.xcor() != -100 or snake2.ycor() != -100:
            game_state = 2
        if game_state == 2:
            time_left = time_left - speed

        # clear the old written score list
        if score > high_score:
            high_score = score
        pen.clear()
        # update score board
        pen.write(f"Score: {score} High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

        timer.clear()
        timer.write(f"Time Left: {round(time_left, 0)}s", align="center", font=("Courier", 24, "normal"))
        if time_left <= ending_time:
            time.sleep(0.5)
            turtle_screen.clear()
            turtle_screen.bgcolor("black")
            endscreen.goto(0, 200)
            endscreen.color("white")
            endscreen.write(f'Your score was {score} \n'
                            f'Highscore was {high_score}', align="center", font=("Courier", 40, "normal"))
            g(-200, 100)
            a(-150, 0)
            m(0, 0)
            e(250, 100)

            o(-300, -150)
            v(-150, -50)
            e(100, -50)
            r(150, -150)
            time.sleep(2)
            turtle.bye()








