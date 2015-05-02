import urllib
import re
import csv   #bo nie ma biblioteki tsv
#i=0
data=[]
def get_data():
    apfile=urllib.urlopen("http://finance.yahoo.com/q?s=AAPL&ql=0")
    aptext=apfile.read()
    micfile=urllib.urlopen("http://finance.yahoo.com/q?s=MSFT&ql=0")
    mictext=micfile.read()
    sonfile=urllib.urlopen("http://finance.yahoo.com/q?s=SNE&ql=0")
    sontext=sonfile.read()
    bafile=urllib.urlopen("http://finance.yahoo.com/q?s=B&ql=0")
    batext=bafile.read()
    gofile=urllib.urlopen("http://finance.yahoo.com/q?s=GOOG&ql=0")
    gotext=gofile.read()
    fbfile=urllib.urlopen("http://finance.yahoo.com/q?s=FB&ql=0")
    fbtext=fbfile.read()
    pafile=urllib.urlopen("http://finance.yahoo.com/q?s=P&ql=0")
    patext=pafile.read()

    apple='<span id="yfs_l84_aapl">(.+?)</span>'
    microsoft='<span id="yfs_l84_msft">(.+?)</span>'
    sony='<span id="yfs_l84_sne">(.+?)</span>'
    barnes='<span id="yfs_l84_b">(.+?)</span>'
    google='<span id="yfs_l84_goog">(.+?)</span>'
    facebook='<span id="yfs_l84_fb">(.+?)</span>'
    pandora='<span id="yfs_l84_p">(.+?)</span>'

    compap=re.compile(apple)
    compmic=re.compile(microsoft)
    compson=re.compile(sony)
    compba=re.compile(barnes)
    compgo=re.compile(google)
    compfb=re.compile(facebook)
    comppa=re.compile(pandora)

    prap=re.findall(compap,aptext)
    prmic=re.findall(compmic,mictext)
    prson=re.findall(compson,sontext)
    prba=re.findall(compba,batext)
    prgo=re.findall(compgo,gotext)
    prfb=re.findall(compfb,fbtext)
    prpa=re.findall(comppa,patext)

    spis1=[prap,prmic,prson,prba,prgo,prfb,prpa]
    spis2=["Apple","Microsoft","Sony","Barnes","Google","Facebook","Pandora"]


    '''for w in spis1:
        w=[l.replace("'[","") for l in w]
        w=[l.replace("]'","") for l in w]
        return spis1'''


    i=0
    while i<len(spis1):
        a=[spis2[i],spis1[i]]
        data.append(a)
        i+=1
    return data

print get_data()


def save_data(data):
    with open("data.tsv","w") as csvfile:   #csv save to file
        writer = csv.writer(csvfile, delimiter='\t', lineterminator='\n')
        header = ["name", "value"]
        writer.writerow(header)
        for line in data:
            writer.writerow(line)

data = get_data()
save_data(data)
