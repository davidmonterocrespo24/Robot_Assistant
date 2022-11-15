from pprint import pprint
import requests
import pygame
import json

#initialization of window and pygame
pygame.init()
screen_length = 450
screen_height = 300
screen = pygame.display.set_mode((screen_length,screen_height))
pygame.display.set_caption('Current.weather')

#get location from website
#location_url = 'http://freegeoip.net/json'
#location_request = requests.get(location_url)
#location_json = json.loads(location_request.text)
lat = -34.90328
lon = -56.18816

#get data from OPENWEATHERMAP API
api_key = "baa52f604cd5a7a0162fafcbc80e677c"
weather_url = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) \
	+ "&units=metric&APPID=" + api_key
w = requests.get(weather_url)
weather = w.json()


#variables that store weather specifics
cityName = weather['name']
temp_current = weather['main']['temp']
temp_min = weather['main']['temp_min']
temp_max = weather['main']['temp_max']
description = weather['weather'][0]['description']
weather_type = weather['weather'][0]['main']
wind = weather['wind']['speed']
picture_code = str(weather['weather'][0]['icon'])

#colours and font
white = (255,255,255)
black = (0,0,0)
text_font_large = pygame.font.Font(None,70)
text_font_small = pygame.font.Font(None,30)


#initialization of all images
clearskyday = pygame.image.load('WeatherApp-Python-master/clearskyday.jpg')
clearskynight = pygame.image.load("WeatherApp-Python-master/clearkskynight.jpg")
fewcloudsday = pygame.image.load("WeatherApp-Python-master/fewcloudsday.jpg")
fewcloudsnight = pygame.image.load("WeatherApp-Python-master/fewcloudsnight.jpg")
scatteredcloudsday = pygame.image.load("WeatherApp-Python-master/scatteredcloudsday.jpg")
scatteredcloudsnight = pygame.image.load("WeatherApp-Python-master/scatteredcloudsnight.jpg")
brokencloudsday = pygame.image.load("WeatherApp-Python-master/brokencloudsday.jpg")
brokencloudsnight = pygame.image.load("WeatherApp-Python-master/brokencloudsnight.jpg")
rainday = pygame.image.load("WeatherApp-Python-master/rainday.jpg")
rainnight = pygame.image.load("WeatherApp-Python-master/rainnight.jpg")
thunderstormday = pygame.image.load("WeatherApp-Python-master/thunderstormday.jpg")
thunderstormnight = pygame.image.load("WeatherApp-Python-master/thunderstormnight.jpg")
snowday = pygame.image.load("WeatherApp-Python-master/snowday.jpg")
snownight = pygame.image.load("WeatherApp-Python-master/snownight.jpg")
mist = pygame.image.load("WeatherApp-Python-master/mist.jpg")

#matching of images and API code
imageDictionary = {
	"01d": clearskyday,
	"01n": clearskynight,
	"02d": fewcloudsday,
	"02n": fewcloudsnight,
	"03d": scatteredcloudsday,
	"03n": scatteredcloudsnight,
	"04d": brokencloudsday,
	"04n": brokencloudsnight,
	"09d": rainday,
	"09n": rainnight,
	"10d": rainday,
	"10n": rainnight,
	"11d": thunderstormday,
	"11n": thunderstormnight,
	"13d": snowday,
	"13n": snownight,
	"50d": mist,
	"50n": mist
}

#reformats all pictures to one size
for x in imageDictionary:
	imageDictionary[x] = pygame.transform.scale(imageDictionary[x],(450,300))


"""
GENERAL FUNCTION DESCRIPTION 
____________________________
All functions display the corresponding data on the screen in a particular place.
The names of the function give a general idea of what will be executed.
"""
def mainTemp(temp_current):
	text = text_font_large.render(str(temp_current) + u"\u00b0", 1, white)
	textPos = (10, 10)
	screen.blit(text, textPos)

def minTemp(temp_min):
	text = text_font_small.render("L: " + str(int(temp_min)) + u"\u00b0", 1, white)
	textPos = (10,60)
	screen.blit(text,textPos)

def maxTemp(temp_max):
	text = text_font_small.render("H: " + str(int(temp_max)) + u"\u00b0", 1, white)
	textPos = (70,60)
	screen.blit(text,textPos)

def descriptionText(description):
	text = text_font_small.render(description, 1, white)
	textPos = (2,280)
	screen.blit(text,textPos)	

def windSpeed(wind):
	text = text_font_small.render(str(int(wind)) + "km/h", 1, white)
	textPos = (375,280)
	screen.blit(text,textPos)


image = imageDictionary[picture_code]
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	screen.blit(image,(0,0))
	mainTemp(temp_current)
	minTemp(temp_min)
	maxTemp(temp_max)
	descriptionText(weather_type)
	windSpeed(wind)

	pygame.display.update()


