from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests
    
    api_request = requests.get("{generated_url_here}")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."
        
 
    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
