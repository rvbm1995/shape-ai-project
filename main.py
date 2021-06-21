import requests

from datetime import datetime

api_key = '8416f7c57b06a0cd02cf35f5964fb850'
location = input('Enter your city name = ')

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp'])-273.15)
weather_desc = api_data['weather'][0]['description']
hmdt =api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

doc_of_data =open("Data_doc.txt","w")
doc_of_data.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
doc_of_data.write ("Current temperature is: {:.2f} deg C".format(temp_city)+"\n")
doc_of_data.write ("Current weather desc  :"+ weather_desc +"\n")
doc_of_data.write("Current Humidity      :"+str(hmdt)+ '% \n')
doc_of_data.write("Current wind speed    :"+str(wind_speed)+ 'kmph')