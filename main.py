from turtle import Screen,Turtle
from snake import Snake
import time

"""Setup screen """
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Anaconda")
screen.tracer(0)

screen.update()

game_on = True
while game_on:
   time.sleep(0.1)

   screen.update() #update only when all three segments have moved forward

screen.exitonclick()