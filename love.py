import turtle #Importing Turtle module
import math  #Importing Math Module

#equation of love function
#It is a parametric  function
#you will see the eqution in right side
#We need to import math module
def lovecurve(t):
    x = 16 * (math.sin(t) ** 3)
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
    return x,y # it will return a tuple


turtle.setup(800,800) #Screen size of turtle drawing
turtle.title("Love Drawing") #Canvas name
turtle.bgcolor("black") #Background color
turtle.pensize(2) #width of line
turtle.pencolor("red") #line color
turtle.speed(0.1) #it will fast the drawing

factor = 20
# Now its time to draw the love curve
turtle.penup() #it removes the first line from center
for i in range(0,400):
    x, y = lovecurve(i) # x,y are the co-ordinates
    turtle.goto(x * factor , y * factor)
    turtle.pendown()
turtle.getcanvas().postscript(file="lovedrawing.eps")
turtle.exitonclick()