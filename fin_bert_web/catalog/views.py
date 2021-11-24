from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
import random
# Create your views here.
def index(request):
    names = ["bob", "dan", "jack", "lizzy", "susan"]
    return render(request, 'index.html', {'names':names})

def report(request):
    
    return render(request, 'report.html')


