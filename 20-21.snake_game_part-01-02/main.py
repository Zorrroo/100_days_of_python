from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Nokia Snake in python")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Detect collision
    if snake.head.distance(food) < 50:
        food.refresh()
        snake.extend()  
        scoreboard.refresh_score()
        
        
# Detect Wall
    if snake.head.xcor() > 295 or snake.head.ycor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() < -295:
        game_is_on = False
        scoreboard.game_over()
        
#Detect collision with tail
    # for segment in snake.segments:#without slicing 
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
    
#slicing 
#     list = [1,2,3,4,5,67,8,9]
#     print(list[1::2])

  #using slicing
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game_is_on = False
            scoreboard.game_over() 
screen.exitonclick()
