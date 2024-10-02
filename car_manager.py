import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# cars are 20px by 40
# randomly generated along y axis, moving from positive to negative x axis
# top and bottom 50px cannot have cars

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300,(random.randint(-250,250)))
            self.all_cars.append(new_car)
        self.move_cars()
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)
    def level_up(self):
            self.speed += MOVE_INCREMENT
