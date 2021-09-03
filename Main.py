#from turtle import * # Import all elements of the turtle library
import json
import urllib
import os
import requests

pokiUrl= "https://pokeapi.co/api/v2/pokemon/ditto"
swapiUrl = "https://swapi.dev/api/people"


pokiInfo = requests.get(pokiUrl)
#print("HTTP Status Code: " + str(pokiInfo.status_code))
#print(pokiInfo.headers)
pokiResponse = json.loads(pokiInfo.content)
print("Pokemon Name: " + pokiResponse["sprites"]["back_default"])

swapiInfo = requests.get(swapiUrl)
swapiResponse = json.loads(swapiInfo.content)

print("Name: " + swapiResponse["results"][1]["name"])

response = requests.get(pokiResponse["sprites"]["back_default"])

file = open("pokiBack.png", "wb")
file.write(response.content)
file.close()

"""
#pokiJson = json.loads(pokiresponse.read())

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
screen.addshape('download.gif')
kingTurt.shape('download.gif')

h=input("press close to exit") 
"""
