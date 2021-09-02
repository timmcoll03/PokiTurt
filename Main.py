from turtle import * # Import all elements of the turtle library
import json
import urllib
import os

pokiUrl= "https://pokeapi.co/api/v2/pokemon/ditto"
swapiUrl = "https://swapi.dev/api/people/1/"



pokiresponse = urllib.urlopen(pokiUrl)
#pokiJson = json.loads(pokiresponse.read())

print(pokiresponse)

swapiresponse = urllib.urlopen(swapiUrl)
swapiJson = json.loads(swapiresponse.read())

print(swapiresponse)


#print (pokiJson)

print (swapiJson["name"])

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
