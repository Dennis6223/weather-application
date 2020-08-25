from django.shortcuts import render
from .models import *
from .forms import CityForm

import requests
# Create your views here.
def front(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=15c7428de186d8fa382178d549086b7c'
        
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    weather_data = []
    try:
        for city in cities:
            r = requests.get(url.format(city)).json()

            city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            }

            weather_data.append(city_weather)
    except KeyError:
        pass
    except EXCEPTION as e:
        pass

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/front.html', context)