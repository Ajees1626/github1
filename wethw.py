import os
from langchain_community .utilities import OpenWeatherMapAPIWrapper
os.environ["OPEN_WEATHERMAP_APIKEY"] ="AIzaSyBBbcF7Ph1-K6mHZa1VO5lOYAfV9vHc-VA"
weather = OpenWeatherMapAPIWrapper()
#location = input("enter the location : ")
result = weather.run("ooty")










