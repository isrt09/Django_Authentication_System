from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	data = {}
	return render(request, 'base.html', context= data)