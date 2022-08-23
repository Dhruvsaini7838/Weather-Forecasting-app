from multiprocessing import context
from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    if request.method =="POST":
        name = request.POST['city']
        # city="Switzerland"
        url=f'https://api.openweathermap.org/data/2.5/weather?q={name}&appid=d1abe75ba7d7b8ff95bf8c7c678cd459'
        data = requests.get(url).json()
        payload ={'city':data['name'],
            'weather': data['weather'][0]['main'],
            'icon': data['weather'][0]['icon'],
            'kelvin_tempreature': data['main']['temp'],
            'celsius_tempreature': data['main']['temp'] - 273,
            'pressure': data['main']['pressure'] ,
            'humidity':data['main']['humidity']
            }
        context={'data':payload}
        return render(request,"home.html",context)
    return render(request,"home.html")    

    
    
    
