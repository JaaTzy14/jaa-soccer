from django.shortcuts import render

# Create your views here.

def show_main(request):
    context =  {
        'appName': "Jaa Soccer",
        'name': "Mirza Radithya Ramadhana",
        'NPM': 2406405563,
        'class': "PBP B"
    }
    return render(request, "main.html", context)