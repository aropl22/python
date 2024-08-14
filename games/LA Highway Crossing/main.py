from turtle import Turtle, Screen
from environment import Environment
from madman import Madman
from cars import Car
from score import Score
import time
import random

### Screen 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
#STARTX = 400
#STARTY = 400
#STARTX = None
#STARTY = None
COLOR = "black"
TITLE = "LA Highway Crossing"

cars = []
available_cars = []
level = 1

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
#screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, startx=STARTX, starty=STARTY)
screen.bgcolor(COLOR)
screen.title(TITLE)
screen.colormode(255)
screen.tracer(0)

road = Environment(SCREEN_WIDTH, SCREEN_HEIGHT)
road.draw_street()

madman = Madman(SCREEN_WIDTH, SCREEN_HEIGHT)
madman.start()

score = Score()

traffic = {key:[] for key in road.car_lines}   #create dictionary with keys from car_lines list and empty lists as values

for pos in range(0,29):
    car = Car()
    cars.append(car)

available_cars = cars[0:] # temp list of cars

# append cars values to lines keys in traffic dictionary

for key in traffic:
    index = 0
    temp_list = []
    for value in available_cars:
        if index < 4:
            traffic[key].append(value)
            #value.free = False
            index += 1
            temp_list.append(value)
    for items in temp_list:
        available_cars.remove(items)

# listen for UP key press       

screen.listen()
screen.onkey(madman.move_up, "Up")

game_on = True

speed_level = 0

while game_on:

    for car in cars[0:29]:
        sleep = 0.05
        time.sleep(sleep)
        if car.free:
            proposed_placement = random.choice(road.car_lines)    
            car.car_placement(road.screen_width,proposed_placement)
            time.sleep(random.uniform(0.03,0.09))
            if car.distance(traffic[proposed_placement][-1]) > 200:
                traffic[proposed_placement].append(car)
                car.free = False
            else: 
                car.goto(SCREEN_WIDTH/2+30, SCREEN_HEIGHT/2+30)
                car.free = True

            car.car_move()
            screen.update()
        else:
            car.car_move()

        if car.xcor()<-400:
            car.free = True

    if madman.ycor() > 300:
        score.level += 1
        madman.goto(0,-SCREEN_HEIGHT/2+18)
        score.score_update()
    
    for car in cars:
        if not car.free and madman.distance(car) < 40:
            game_on = False
            score.game_over()
            
         
    screen.update()
screen.onkey(madman.do_nothing, "Up")  

screen.exitonclick()
