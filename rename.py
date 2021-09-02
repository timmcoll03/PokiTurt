from turtle import * # Import all elements of the turtle library
import json
import urllib
import os

testimg = "python2.png"
base = os.path.splitext(testimg)[0]
os.rename(testimg, base + '.gif')