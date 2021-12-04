from turtle import Turtle

starting_pos = [(0,0),(-20,0),(-40,0)]

class Snake():

   def __init__(self):
      self.snake = []

   def createTurtle(self,pos):
      turt = Turtle("square")
      turt.color("white")
      turt.pu()
      turt.goto(pos)
      return turt
   
   def createSnake(self):
      for pos in starting_pos:
         self.snake.append(self.createTurtle(pos))
   
   def move(self):
      for sn in range(len(self.snake) - 1, 0, -1):
         new_x = self.snake[sn-1].xcor()
         new_y = self.snake[sn-1].ycor()
         self.snake[sn].goto(new_x,new_y)
      self.snake[0].forward(20)   