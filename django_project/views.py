from django.shortcuts import render

# Create your views here.
def home(request):
  name = request.GET.get('name')
  return render(request, 'index.html', {'name': name})
