import turtle
import time
import os
import random

delay=0.1
score=0
highscore=0

 #Set up the screen
so=turtle.Screen()
so.title("Snakessssss")
so.bgcolor("green")
so.setup(width=600,height=600)
so.tracer(0)  #turns off screen updates


#Snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"


#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0 High Score:0",align="center",font=("Courier",24,"italic"))


#Moving the head
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

def goup():
    if head.direction!="down":
        head.direction="up"

def godown():
    if head.direction!="up":
        head.direction="down"

def goleft():
    if head.direction!="right":
        head.direction="left"

def goright():
    if head.direction!="left":
        head.direction="right"


#Keyboard bindings
so.listen()
so.onkeypress(goup,"Up")
so.onkeypress(godown,"Down")
so.onkeypress(goleft,"Left")
so.onkeypress(goright,"Right")

    
        
#Food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


#Snake-body
segments=[]


#Main game loop
while True:
    so.update()

    #Check for border collisions
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #Hide segments

        for segment in segments:
            segment.goto(1000,1000)

        #Clear segments
        segments.clear()


        #Reset delay
        delay=0.1
        
        #Update Score
        score=0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,highscore),align="center",font=("Courier",24,"bold"))

    #Increasing size
    if(head.distance(food)<20):
        #Move to a random position
        x=random.randint(-270,270)
        y=random.randint(-270,270)
        food.goto(x,y)

        #Add a segment
        newseg=turtle.Turtle()
        newseg.speed(0)
        newseg.shape("square")
        newseg.color("grey")
        newseg.penup()
        segments.append(newseg)

        #Shorten time delay
        delay-=0.001

        score+=10

        if score>highscore:
            highscore=score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,highscore),align="center",font=("Courier",24,"bold"))

    #Move segments
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    #Move segment 0 to head
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    
        
        
        
    move()

    #Check for head-body collisions
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            #Hide segments

            for segment in segments:
                segment.goto(1000,1000)

            #Clear segments
            segments.clear()

            #Update Score
            score=0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score,highscore),align="center",font=("Courier",24,"bold"))
            
            delay=0.1        
    
    time.sleep(delay)
    
    




so.mainloop()
