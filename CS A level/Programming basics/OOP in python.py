from turtle import Turtle
from random import randint      # this line helps us generate random integers
tilly = Turtle()
tilly.color('blue')        #gives tilly a colour
tilly.shape('turtle')       #gives tilly a turtle shape
#We can also tell our Turtle (tilly) object what to do by calling other methods.
# With the code below, we are instructing the object to stop drawing with penup(),
# then to move to a location with goto(),
# and finally to get ready to draw a line with pendown().
tilly.penup()
tilly.goto(-160, 50)
tilly.pendown()
rik = Turtle()              #creates a new turtle object with the same attributes but with a new name
rik.color('green')
rik.shape('turtle')
rik.penup()
rik.goto(-160,100)
rik.pendown()
irene = Turtle()
irene.color('purple')
irene.shape('turtle')
irene.penup()
irene.goto(-160,150)
irene.pendown()
molly = Turtle()
molly.color('yellow')
molly.shape('turtle')
molly.penup()
molly.goto(-160,200)
molly.pendown()
#adding code to make the turtle objects race
for movement in range(100):
    tilly.forward(randint(1,5))
    rik.forward(randint(1,5))
    irene.forward(randint(1,5))             #the forward method asks the turtles to move forward by a random integer between 1 and 5
    molly.forward(randint(1,5))             #we are calling a method on each

input("Press enter to close")
