'''
data = open("rand100_collections.txt",'r')

#company = "26076"
#year = "2018"

itemlist = ["Item1","Item1A","Item1B","Item2",
            "Item3","Item4","Item5","Item6","Item7",
            "Item7A","Item8","Item9","Item9A","Item9B",
            "Item10","Item11","Item12","Item13","Item14",
            "Item15"]
textdic = {}
for line in data.readlines():
    line1 = line.split("\t")
    #line1[0]: id
    #line1[1]: sentence
    textdic[line1[0]] = line1[1]
'''

def read_allitem_fun(textdic,company,year):
    #find the first one id
    articleid = []
    article = []
    textkeys = list(textdic.keys())
    firstidx = company+"_"+str(year).split("20")[1]+"_"+"item1".upper()+"_P"+str(0)+"_S"+str(0)
    if firstidx not in textkeys:
        for item in itemlist[1:len(itemlist)]:
            firstidx = company+"_"+str(year).split("20")[1]+"_"+item.upper()+"_P"+str(0)+"_S"+str(0)
            if firstidx in textkeys:
                firstline_item = item

                break
    else:
        firstline_item = itemlist[0]

    lastone = textkeys[len(textkeys)-1]
    lastcompany = lastone.split("_")[0]
    lastyear = lastone.split("_")[1]
    #print(lastyear,lastcompany)
    #if it is the last company or year
    if company==lastcompany and year.split("20")[1]==lastyear:
        for item in itemlist[itemlist.index(firstline_item):len(itemlist)]:
            idx = company+"_"+str(year).split("20")[1]+"_"+item.upper()+"_P"+str(0)+"_S"+str(0)
            if idx not in textkeys:
                articleid.append("no item")
            else:
                for i in range(textkeys.index(idx),len(textkeys)):
                    articleid.append(textkeys[i])
    else:
        for item in itemlist[itemlist.index(firstline_item):len(itemlist)]:
            idx = company+"_"+str(year).split("20")[1]+"_"+item.upper()+"_P"+str(0)+"_S"+str(0)
            if idx not in textkeys:
                articleid.append("no item")
            else:
                for i in range(textkeys.index(idx),len(textkeys)):
                    articleid.append(textkeys[i])
                    if (textkeys[i+1].split("_")[2]!=item.upper()):
                        break
    if firstline_item != itemlist[0]:
        for item in itemlist[:itemlist.index(firstline_item)]:
            article.append("There is no "+str(item)+" in "+str(year))
            article.append("\\n")
            article.append("\\n")
    #print(textdic[articleid[404]])
    #textdic["no item"] ==?

    for i in range(0,len(articleid)):
        if articleid[i] == "no item":
            article.append("There is no "+str(item)+" in "+str(year))
            article.append("\\n")
            article.append("\\n")
        else:
            a = textdic[articleid[i]].strip("\n")
            a = a.replace('"',"")
            a = a.replace("'","")
            article.append(a)
            nowp = articleid[i].split("_")[3]
            if (i!=(len(articleid)-1)):
                if articleid[i+1] == "no item":
                    article.append("\\n")
                    article.append("\\n")
                else:
                    nextp = articleid[i+1].split("_")[3]
                    if(nextp!=nowp):
                        article.append("\\n")
                        article.append("\\n")

    return article
    #append id in the articleid
    #build up article
        #if firstitem != item1
        #insert "there is no item in year" in the beginning of the list
    #return article
#print(read_allitem_fun(textdic,company,year))
