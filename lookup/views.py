from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests
    
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=92078&distance=30&API_KEY=F3F8D30B-21B1-42AA-939A-8CD6BE83F86D")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."
        
 
    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
