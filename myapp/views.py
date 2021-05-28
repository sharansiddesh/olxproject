from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def motorcycle(request):
    return render(request,'motorcycle.html')

def house(request):
    return render(request,'house&aparments.html')

def scooters(request):
    return render(request,'scootes.html')

def commercial(request):
    return render(request,'commercial&other vehicales.html')

def mobilephone(request):
    return render(request,'mobilephone.html')