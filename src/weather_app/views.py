from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    personal = "715fb00ac17f68b9dc097078e1299f7c"
    city = None

    if request.method == "POST":
        city = request.POST.get('city')
        API = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={personal}&units=metric"

        response = requests.get(API)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']
            weather_icon = data['weather'][0]['icon']

            context = {
                'city': city,
                'temp': temperature,
                'weather_description': weather_description,
                'weather_icon': weather_icon,
            }

            return render(request, 'index.html', context)
        
        else:
            return render(request, 'index.html')
    else:
        return render(request, 'index.html',)



