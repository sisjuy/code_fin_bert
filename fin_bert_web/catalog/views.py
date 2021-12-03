from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
import random
# Create your views here.
def index(request):
    names = ["abc", "dan", "jack", "lizzy", "susan"]
    return render(request, 'index.html', {'names':names})

import os
#from . import test

# create highlight sentence and score
def teammate():
    sen = {"senA":"I am a student","senB":"I am a teacher","keywordsA":[],"keywordsB":["teacher"],"labels":[0,0,0,1]}
    return sen

def report(request):
    if request.method == "POST":
        module_dir = os.path.dirname(__file__)
        company = request.POST.get("company")
        year2 = int(request.POST.get("year"))
        year1 = year2-1
        filename = company + '.txt'
        file_path1 = os.path.join(module_dir,"dataset",str(year1),filename)   #full path to text.
        file_path2 = os.path.join(module_dir,"dataset",str(year2),filename)
        data_file1 = open(file_path1,'r')
        data_file2 = open(file_path2,'r')
        data1 = data_file1.read() #selected year-1
        data2 = data_file2.read() #selected year 

        #highlight
        result = teammate()
        #senA = result['senA']
        #senB = result['senB']
        #keywordsB = result['keywordsB']
        #labels = result['labels']
        #'senA':senA, 'senB':senB, 'keywordsB':keywordsB,'labels':labels
        context = {'data1': data1, 'data2':data2, 'result':result}
        return render(request, 'report.html',context)
    
    return render(request, 'report.html')


