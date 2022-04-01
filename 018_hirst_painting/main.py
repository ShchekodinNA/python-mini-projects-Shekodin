import colorgram
import random
from turtle import Turtle, Screen

# colors_loaded = colorgram.extract('spot_painting.jpg', 36)
colors = [(211, 154, 98), (241, 248, 246), (236, 241, 245), (53, 107, 131),
          (177, 78, 34), (199, 142, 34), (116, 156, 171), (123, 80, 98), (124, 175, 157), (226, 197, 130),
          (190, 88, 110), (55, 38, 19), (12, 49, 63), (43, 168, 128), (51, 126, 121), (197, 124, 143),
          (166, 21, 31), (222, 93, 79), (243, 163, 160), (38, 32, 35), (4, 25, 24), (80, 147, 168), (161, 26, 23),
          (19, 79, 92), (233, 167, 172), (175, 207, 187), (101, 127, 158), (165, 203, 210), (61, 60, 72),
          (13, 107, 104), (181, 190, 205), (80, 66, 38)]
# for color in colorgram.extract('spot_painting.jpg', 36):
#     colors.append(
#         (color.rgb[0], color.rgb[1], color.rgb[2])
#     )
X_BEGIN = -200
Y_BEGIN = -200
DOT_SIZE = 157
GAP = 50

tim = Turtle()
tim.speed(0)
tim.hideturtle()
screen = Screen()
screen.colormode(255)
tim.up()
tim.goto(X_BEGIN, Y_BEGIN)
for i in range(1, 11):
    for j in range(10):
        tim.dot(DOT_SIZE, random.choice(colors))
        tim.forward(GAP)
    tim.goto(X_BEGIN, Y_BEGIN + i * 50)
screen.exitonclick()
