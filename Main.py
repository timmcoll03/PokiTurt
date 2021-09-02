from turtle import * # Import all elements of the turtle library


# Set up the graphics window:
screen = Screen()
screen.setup(1000, 1000)
screen.bgcolor(0, 0, 0)
colormode(255)

# Create a turtle object and set some of its attributes:
kingTurt = Turtle()
kingTurt.shape("turtle")
kingTurt.resizemode("auto")
kingTurt.width(3)
kingTurt.pencolor("blue")
kingTurt.speed(0)

#Re-creates turtle sprite image as python2 gif 
screen.addshape('python2.gif')
kingTurt.shape('python2.gif')

h=input("press close to exit") 