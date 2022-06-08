### teammate function
path

```python
fin_bert_web/catalog/view.py
```

senA / senB / labels(score) format:
```python

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
},

"2013":{

"Item1":
[{"senA": "i am a student", "senB": "i am a teacher", "labels": "[0,0,0.5,0.6]"},
{....},
{....}],

"Item1A":
[{....},
{....},
{....}]
}

}
```

### add company list
```python
fin_bert_web/catalog/templates/report.html
```
##### search
```
var vm1 = new Vue
```
