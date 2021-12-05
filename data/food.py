from turtle import Turtle
import random
COLOR = "yellow"
SHAPE = "turtle"

class Food(Turtle):
   def __init__(self):
      super().__init__()
      self.shape(SHAPE)
      self.shapesize(stretch_len=0.5, stretch_wid=0.5)
      self.color(COLOR)
      self.speed("fastest")
      self.pu()
      self.consumed()

   def consumed(self):
      x = random.randint(-280,280)
      y = random.randint(-280,280)
      self.goto(x,y)
      
   

