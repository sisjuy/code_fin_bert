from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
import random
# Create your views here.
def index(request):
    names = ["abc", "dan", "jack", "lizzy", "susan"]
    return render(request, 'index.html', {'names':names})

import os

    
def report(request):
    if request.method == "POST":
        module_dir = os.path.dirname(__file__)
        company = request.POST.get("company")
        year = request.POST.get("year")
        filename = company + '.txt'
        file_path = os.path.join(module_dir,"dataset",year,filename)   #full path to text.
        data_file = open(file_path , 'r')       
        data = data_file.read()
        context = {'rooms': data}
        return render(request, 'report.html',context)
    
    return render(request, 'report.html')


