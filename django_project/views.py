from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'index.html')

def welcome(request, name):
  name = name
  return render(request, 'welcome.html', {'name': name})