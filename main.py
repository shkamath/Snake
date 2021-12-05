from turtle import Screen
from data.snake import Snake
from data.food import Food
from data.score import ScoreBoard
import time

"""Setup screen """
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Anaconda")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

def detect_wall_collision():
   if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
      return False
   else:
      return True

def detect_tail_collision():
   ret_val = True
   for segment in snake.snake[1:]:
      if snake.head.distance(segment) < 10:
         ret_val &= False
      else:
         ret_val &= True
   return ret_val

game_on = True
while game_on:
   time.sleep(0.2)
   screen.update()
   snake.move()
   game_on &= detect_wall_collision()
   game_on &= detect_tail_collision()
   if game_on == False:
      score.game_over()

   #Detect food intake
   if snake.head.distance(food) < 14:
      snake.grow()
      food.consumed()
      score.update_score()

screen.exitonclick()