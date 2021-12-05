from turtle import Turtle
FONT = ('Courier',20,'normal')
ALIGNMENT = "center"

class ScoreBoard(Turtle):
   def __init__(self):
      super().__init__()
      self.color("white")
      self.speed("fastest")
      self.pu()
      self.goto(0,275)
      self.hideturtle()
      self.score = 0
      self.write(f"Score: {self.score}", align=ALIGNMENT, font= FONT)

   def update_score(self):
      self.clear()
      self.score += 1
      self.write(f"Score: {self.score}", align=ALIGNMENT, font= FONT)
   
   def game_over(self):
      self.goto(0,0)
      self.write("GAME OVER :(",align=ALIGNMENT, font= FONT)