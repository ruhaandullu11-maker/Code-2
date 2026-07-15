import time
import turtle
import random

t = turtle.Turtle()
t.shape('square')
t.color("blue")

numfoods = 10
foodlist = []

for aa in range(numfoods):
    foods = turtle.Turtle()
    print(foods)
    foods.penup()
    foods.speed(0)
    foods.shape('square')
    foods.color('black')
    foods.goto(random.randint(-200, 200), random.randint(-200, 200))
    foodlist.append(foods)

pen = turtle.Turtle()
pen.penup()
pen.goto(180, 180)
pen.color("white")
pen.ht()

report = turtle.Turtle()
report.penup()
report.goto(0, 0)
report.color("white")
report.ht()

start = 0

def right():
    if t.heading() != 180.0:
        t.setheading(0.0)


def left():
    if t.heading() != 0.0:
        t.setheading(180.0)


def up():
    if t.heading() != 270.0:
        t.setheading(90.0)


def down():
    if t.heading() != 90.0:
        t.setheading(-90.0)




steps = 0

ts = t.screen
ts.bgcolor("magenta")

ts.onkey(right, "Right")
ts.onkey(left, "Left")
ts.onkey(up, "Up")
ts.onkey(down, "Down")
ts.listen()

catch = [False] * numfoods

segs = []

gameover = False

while gameover == False:
	steps = steps + 1
	pen.write(len(segs), align="center", font=("Courier", 24, "normal"))
    
	for aa in range(len(foodlist)):
		if not catch[aa]:			
			if t.distance(foodlist[aa]) < 20:
				catch[aa] = True
				foodlist[aa].color('green')
				segs.append(foodlist[aa])
				pen.clear()
                    


	for index in range(len(segs) - 1, 0, -1):
		x = segs[index - 1].xcor()
		y = segs[index - 1].ycor()
		segs[index].goto(x, y)

   

	if len(segs) > 0:
		xcor = t.xcor()
		ycor = t.ycor()
		segs[0].st()
		segs[0].goto(x , y)
	
	t.forward(20)
    
	
	if t.xcor() > 10:
		started = 1
		
	if len(segs) == numfoods:
		if abs(t.xcor()) < 20 and abs(t.ycor()) < 20:
			game_over = True
			time.sleep(1)
			t.clear()
			t.ht()
			for kk in range(len(segs)):
				segs[kk].ht()
				
			report.write("Steps Taken: " + str(steps),align="center",font=("Courier", 24, "normal"))
	
	time.sleep(0.1)