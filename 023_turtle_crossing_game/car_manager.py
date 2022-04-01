from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCR = 10
NEW_CAR_LENGTH = 40
CAR_SHAPE = "square"


class CarManager:
    def __init__(self, list_of_start_y, num_of_cars, collision_object):
        self.list_of_start_y = list_of_start_y
        self.num_of_cars = num_of_cars
        self.starting_car_speed = MOVE_INCR
        self.collision_object = collision_object
        self.list_of_cars = []
        self.half_of_screen_width = Turtle().getscreen().window_width() // 2
        self.create_cars()

    def create_cars(self):
        for _ in range(self.num_of_cars):
            self.create_car()

    def create_car(self):

        new_car = Turtle(shape=CAR_SHAPE)
        self.list_of_cars.append(new_car)
        new_car.up()
        new_car.shapesize(stretch_len=NEW_CAR_LENGTH / 20)
        self.reformat_car(car_obj=new_car)
        new_car.goto((random.randint(-self.half_of_screen_width + 50, self.half_of_screen_width), new_car.pos()[1]))

    def reformat_car(self, car_obj):
        line = random.choice(self.list_of_start_y)
        color = random.choice(COLORS)
        car_obj.speed(0)
        car_obj.color(color)
        car_obj.goto((self.half_of_screen_width + 20, line))
        car_obj.speed(self.starting_car_speed)

    def randomize_all_car_pos(self):
        for car in self.list_of_cars:
            car.goto((random.randint(-self.half_of_screen_width + 50, self.half_of_screen_width), car.pos()[1]))

    def move_all_cars(self):
        for car in self.list_of_cars:
            if car.pos()[0] <= -self.half_of_screen_width - 40:
                self.reformat_car(car_obj=car)
            car.backward(self.starting_car_speed)

    def is_have_collision(self):
        for car in self.list_of_cars:
            if car.distance(self.collision_object) < NEW_CAR_LENGTH // 2 + 10 \
                    and car.pos()[1] + 10 >= self.collision_object.pos()[1]:
                return True
        return False
