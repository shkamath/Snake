from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
SNAKE_STEP_SIZE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

   def __init__(self):
      self.snake = []
      self.createSnake()
      self.head = self.snake[0]

   def createTurtle(self,pos):
      turt = Turtle("square")
      turt.color("white")
      turt.pu()
      turt.goto(pos)
      return turt
   
   def createSnake(self):
      for pos in STARTING_POSITION:
         self.snake.append(self.createTurtle(pos))
   
   def move(self):
      for sn in range(len(self.snake) - 1, 0, -1):
         new_x = self.snake[sn-1].xcor()
         new_y = self.snake[sn-1].ycor()
         self.snake[sn].goto(new_x,new_y)
      self.snake[0].forward(SNAKE_STEP_SIZE)   
   
   def up(self):
      if self.head.heading() != DOWN:
         self.head.seth(UP)
   
   def down(self):
      if self.head.heading() != UP:
         self.head.seth(DOWN)
   
   def left(self):
      if self.head.heading() != RIGHT:
         self.head.seth(LEFT)
   
   def right(self):
      if self.head.heading() != LEFT:
         self.head.seth(RIGHT)