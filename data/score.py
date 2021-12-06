from turtle import Turtle
FONT = ('Courier',20,'normal')
ALIGNMENT = "center"
SCORE_FILE_PATH="./data/high_score_data.txt"

class ScoreBoard(Turtle):
   def __init__(self):
      super().__init__()
      self.color("white")
      self.speed("fastest")
      self.pu()
      self.goto(0,275)
      self.hideturtle()
      self.score = 0
      self.highscore = self.get_high_score_record()
      self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font= FONT)

   def update_score(self):
      self.clear()
      self.score += 1
      self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font= FONT)
   
   def game_over(self):
      self.goto(0,0)
      self.write("GAME OVER :(",align=ALIGNMENT, font= FONT)
   
   def reset(self):
      if self.score > self.highscore:
         self.highscore = self.score
      self.score = 0
      self.update_score()
      self.create_high_score_record()

   def create_high_score_record(self):
      with open(SCORE_FILE_PATH,mode="w") as file:
         file.write(f"{self.highscore}")
   
   def get_high_score_record(self):
      score = 0
      try:
         with open(SCORE_FILE_PATH,mode="r") as file:
            score = int(file.read())
      except:
         print("File for high score does not exist. Creating one now")
         with open(SCORE_FILE_PATH,mode="w") as file:
            pass
      return score
