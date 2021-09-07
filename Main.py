#from turtle import * # Import all elements of the turtle library
import json
import urllib
import os
import requests
from PIL import Image 
import random

pokiNumberGlobal = 0
im = [0] * 10



def pokiImage(num):#this function will create a new pokiImage thats name is synced with [pokiNumberGlobal+1] 
    pokiNum = str(random.randint(1,1000))
    pokiUrl= "https://pokeapi.co/api/v2/pokemon/"
    pokiUrl += pokiNum
    pokiInfo = requests.get(pokiUrl)
    pokiResponse = json.loads(pokiInfo.content)
    print("Pokemon Name: " + pokiResponse["forms"][0]["name"])
    imageResponse = requests.get(pokiResponse["sprites"]["back_default"])
    file = open("pokiImage" +str(0)+ ".png", "wb")
    file.write(imageResponse.content)
    file.close()
    print("image pulled")
    return (pokiNum)

def abilitys(num, tag):
    pokiUrl= "https://pokeapi.co/api/v2/pokemon/"
    pokiUrl += tag
    pokiInfo = requests.get(pokiUrl)
    pokiResponse = json.loads(pokiInfo.content)
    abilitys = ['a'] * 2
    for abl in range(2):
        abilitys[abl] = pokiResponse["abilities"][abl]["ability"]["name"]
        print(abilitys[abl])
    print("abilities pulled")
    return

class PokiMon:  
    def __init__(GlobalNum):
        Tag = pokiImage(GlobalNum)
        imageFileName = "pokiImage" + str(GlobalNum)
        Ability = abilitys(GlobalNum,Tag)

for x in range(2):
    PokiOne = PokiMon()
    im[pokiNumberGlobal] = Image.open(r"/Users/timothycolledge/Desktop/Compsci/PokiTurt/pokiImage"+str(0)+".png")
    im[pokiNumberGlobal].show()






"""


swapiUrl = "https://swapi.dev/api/people"





swapiInfo = requests.get(swapiUrl)
swapiResponse = json.loads(swapiInfo.content)
print("Name: " + swapiResponse["results"][1]["name"])
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
