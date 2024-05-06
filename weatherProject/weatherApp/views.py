from django.shortcuts import render

# Create your views here.
import urllib.request
import json

def index(request): 
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=2d6aac3a17e5a7ebf7182f177968b8a8').read()
        list_of_data = json.loads(source)
        
        data = {
            "city": city,
            "state": list_of_data.get('state', 'N/A'),  # Assuming state is provided in the API response
            "zip_code": list_of_data.get('zip_code', 'N/A'),  # Assuming zip code is provided in the API response
            "country": list_of_data.get('sys', {}).get('country', 'N/A'),  # Extracting country from 'sys' object
            "country_code" : str(list_of_data['sys']['country']),
            "coordinate" : str(list_of_data['coord']['lon']) + ',' + str(list_of_data['coord']['lat']),
            "temp" : str(list_of_data['main']['temp']) + 'F',
            "pressure" : str(list_of_data['main']['pressure']),
            "wind" : str(list_of_data['wind']['speed']),
            "rain" : str(list_of_data.get('rain', {}).get('1h', 'N/A')),
            "clouds" : str(list_of_data['clouds']['all']),
            "humidity" : str(list_of_data['main']['humidity']),
            "main" : str(list_of_data['weather'][0]['main']),
            "description" : str(list_of_data['weather'][0]['description']),
            "icon" : list_of_data['weather'][0]['icon'],
        }
        print(data)
    else:
        data = {}

    return render(request, "main/index.html", data)
