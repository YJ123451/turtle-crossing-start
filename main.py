import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


global game_is_on
game_is_on = True

def game_over():
    end_text = Turtle()
    end_text.color('black')
    end_text.penup()
    end_text.hideturtle()
    end_text.goto(0,0)
    end_text.write("Game Over",align = "center",font = ("Courier", 24, "normal" ))
    global game_is_on
    game_is_on = False



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_over()

    # Detect turtle reaching other side
    if player.ycor() > 280:
        player.goto(0,-280)
        scoreboard.increase_level()
        car_manager.level_up()




screen.exitonclick()