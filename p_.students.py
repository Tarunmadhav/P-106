import csv
import plotly.express as px
import numpy as np
def getdata(data):
    Marks=[]
    Days=[]
    with open(data) as d:
        reader=csv.DictReader(d)
        for i in reader:
            Days.append(float(i["Days Present"]))
            Marks.append(float(i["Marks In Percentage"]))
    return {"x":Days,"y":Marks}
def findcorelation(dataSource):
    corelation=np.corrcoef(dataSource["x"],dataSource["y"])
    print(corelation[0,1])
def setup():
    data="D:\git\Corrilation\Student Marks vs Days Present.csv"
    ds=getdata(data)
    findcorelation(ds)
setup() 