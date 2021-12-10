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
itemlist = ["Item1","Item1A","Item1B","Item2",
            "Item3","Item4","Item5","Item6","Item7",
            "Item7A","Item8","Item9","Item9A","Item9B",
            "Item10","Item11","Item12","Item13","Item14",
            "Item15"]
# create highlight sentence and score
def teammate():
    sen = {"senA":"The Company was incorporated on May 6, 2004.","senB":"The patients in the study were followed for a total of 24 weeks.","keywordsA":[],"keywordsB":["patients"],"labels":[0,0,0,1]}
    return sen
def filecontent(module_dir,company,year,item):
    
    file_path = os.path.join(module_dir,"dataset","rand-10-collections.txt")
    data = open(file_path,'r')
    textdic = {}
    for line in data.readlines():
        line1 = line.split("\t")
        textdic[line1[0]] = line1[1]
    
    textkeys = list(textdic.keys())
    id = company+"_"+str(year).split("20")[1]+"_"+item.upper()+"_P"+str(0)+"_S"+str(0)
    if (id not in textkeys):
        return ["there is no "+str(item)+" in "+str(year)]
    else:
        articleid=[]
        article=[]
        if (item=="Item15" and year=="2018"):
            id1 = company+"_"+str(year).split("20")[1]+"_"+item.upper()+"_P"+str(0)+"_S"+str(0)
            textkeys = list(textdic.keys())
            for i in range(textkeys.index(id1),len(textkeys)):    
                articleid.append(textkeys[i])
        elif (item=="Item15"):
            id1 = company+"_"+str(year).split("20")[1]+"_"+item.upper()+"_P"+str(0)+"_S"+str(0)
            #id2 = company+"_"+str(int(year)+1).split("20")[1]+"_"+itemlist[0].upper()+"_P"+str(0)+"_S"+str(0)
            for i in range(textkeys.index(id1),len(textkeys)):
                articleid.append(textkeys[i])
                if (textkeys[i+1].split("_")[2]!=item.upper()):
                    break
        else:
            item1 = item
            item2 = itemlist[itemlist.index(item)+1]
            id1 = company+"_"+str(year).split("20")[1]+"_"+item1.upper()+"_P"+str(0)+"_S"+str(0)
            #id2 = company+"_"+str(year).split("20")[1]+"_"+item2.upper()+"_P"+str(0)+"_S"+str(0)
            for i in range(textkeys.index(id1),len(textkeys)):
                articleid.append(textkeys[i])
                if (textkeys[i+1].split("_")[2]!=item.upper()):
                    break

        for i in range(0,len(articleid)):
            article.append(textdic[articleid[i]])
            
        return article



def report(request):
    if request.method == "POST":
        module_dir = os.path.dirname(__file__)
        company = request.POST.get("company")
        year2 = int(request.POST.get("year"))
        year1 = year2-1
        item = request.POST.get("item")
        article1 = filecontent(module_dir,company,year1,item)
        article2 = filecontent(module_dir,company,year2,item)
        #filename = company + '.txt'
        #file_path1 = os.path.join(module_dir,"dataset",str(year1),filename)   #full path to text.
        #file_path2 = os.path.join(module_dir,"dataset",str(year2),filename)
        #data_file1 = open(file_path1,'r')
        #data_file2 = open(file_path2,'r')
        #data1 = data_file1.read() #selected year-1
        #data2 = data_file2.read() #selected year 

        #highlight
        result = teammate()
        #senA = result['senA']
        #senB = result['senB']
        #keywordsB = result['keywordsB']
        #labels = result['labels']
        #'senA':senA, 'senB':senB, 'keywordsB':keywordsB,'labels':labels
        context = {'data1': article1, 'data2':article2, 'result':result}
        return render(request, 'report.html',context)
    
    return render(request, 'report.html')

