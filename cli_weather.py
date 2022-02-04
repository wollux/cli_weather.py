import requests
import sys
from rich.console import Console
from rich.table import Table
from rich.live import Live


OPENWEATHERMAP_API_KEY = "USE YOUR OWN!"
OPENWEATHERMAP_API_URL = "https://api.openweathermap.org/data/2.5/weather"

OPENWEATHERMAP_API_METRIC = "metric" #standard, metric and imperial
OPENWEATHERMAP_API_LANG = "en" #see https://openweathermap.org/current#multi


def get_weather_data(get_city):
	request_url = f"{OPENWEATHERMAP_API_URL}?appid={OPENWEATHERMAP_API_KEY}&units={OPENWEATHERMAP_API_METRIC}&lang={OPENWEATHERMAP_API_LANG}&q={get_city}"
	response = requests.get(request_url)
	if response.status_code <= 300:
		response_data = response.json()
		temp = round(response_data['main']['temp'])
		table.add_row(response_data['name']+'/'+response_data['sys']['country'],response_data['weather'][0]['description'], str(temp)+"°", str(response_data['main']['humidity'])+"%")
	else:
		#print (f"Request error: "+str(response.status_code))
		table.add_row(get_city+" / No data",style="red")		
	

table = Table(title="cli_weather.py - data from OpenWeatherMap")
table.add_column("City/Country", justify="left", style="cyan", no_wrap=True)
table.add_column("Description", style="yellow")
table.add_column("Temp", style="blue")
table.add_column("Humidity", justify="right", style="green")

if len(sys.argv) == 1:	
	print('Please give me the cities where you want to query the weather.')
	print('for example: cli_weather.py Berlin "New York" Peking')	
	exit()
else:
	for x in sys.argv[1:]:	
		get_weather_data(x)

console = Console()
console.print(table)





