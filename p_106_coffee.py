import csv
import plotly.express as px
import numpy as np
def getdata(data):
    Coffee=[]
    Sleep=[]
    with open(data) as d:
        reader=csv.DictReader(d)
        for i in reader:
            Sleep.append(float(i["sleep in hours"]))
            Coffee.append(float(i["Coffee in ml"]))
    return {"x":Sleep,"y":Coffee}
def findcorelation(dataSource):
    corelation=np.corrcoef(dataSource["x"],dataSource["y"])
    print(corelation[0,1])
def setup():
    data="D:\git\Corrilation\cups of coffee vs hours of sleep.csv"
    ds=getdata(data)
    findcorelation(ds)
setup() 