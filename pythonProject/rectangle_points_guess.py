import random
import turtle
from random import randint
from turtle import Turtle
class Point:

    def __init__(self , x , y):
        self.x = x
        self.y = y
    def falls_in_rectangle(self,rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
        and rectangle.point1.y <self.y<rectangle.point2.y:
            return True
        else:
            return False

class GuiPoint(Point):
    def draw(self,canvas , size = 5 , color = "red"):
        canvas.penup()
        canvas.goto(self.x ,self.y)
        canvas.pendown()
        canvas.dot(size , color)



class Rectangle:

    def __init__(self, point1 , point2):
        self.point1=point1
        self.point2=point2
    def area(self):
        return((self.point2.x - self.point1.x) + (self.point2.y - self.point1.y))**2


class GuiRectangle(Rectangle):
    def draw(self,canvas):
        canvas.penup()
        canvas.goto(self.point1.x , self.point1.y)
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)

rectangle = GuiRectangle(Point(randint(0,200) ,randint(0,200)),Point(randint(10,200),randint(10,200)))

print("Rectangle Cordinates " ,
      rectangle.point1.x , "," ,
      rectangle.point1.y , " , " ,
      rectangle.point2.x , "," ,
      rectangle.point2.y
      )

user_points = GuiPoint(float(input("enter x cordinate")) , float(input('enter y cordinate')))
user_area = float(input("area"))

print("your points are inside rectangle : ", user_points.falls_in_rectangle(rectangle))
print('your area difference by:', rectangle.area() - user_area)

myturtle = turtle.Turtle()
rectangle.draw(myturtle)
user_points.draw(myturtle)
turtle.done()