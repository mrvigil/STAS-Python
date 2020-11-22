#Turtle graphics game
import turtle
#set up screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")

#Create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.pendown()
#set speed variable
speed=2
while True:
  for i in range(0,50):
    player.forward(speed)
  player.left(111)