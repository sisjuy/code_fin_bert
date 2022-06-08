### put dataset in the folder
```python
fin_bert_web/catalog/dataset
```
#### filename
```
rand100_collections
```


### teammate function
path

```python
fin_bert_web/catalog/view.py
```

senA / senB / labels(score) format:
```python

output = {
"year2" : {

"Item1":
[ 
{"senA": ".....", "senB": ".....", "labels": [0,1,0.5,....]},
{.......},
{.......}
],

"Item1A":
[....],

}
}


#example
sen = {

"2012":{

"Item1":
[{"senA": "i am a student", "senB": "i am a teacher", "labels": "[0,0,0.5,0.6]"},
{....},
{....}],

"Item1A":
[{"senA": "it is a bird", "senB": "it is a cat", "labels": "[0,0,0.5,0.6]"},
{....},
{....}]

}

}
```

### add company list
path:
```python
fin_bert_web/catalog/templates/report.html
```
- find code position by searching "var vm1 = new Vue"
- add company's cik & name based on previous format

### open web

under "fin_bert_web" folder and type
```
python manage.py runserver
```
