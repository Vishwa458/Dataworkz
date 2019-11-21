from django.db import models
from dateutil.parser import parse
import json
class Stock(models.Model):
    Date = models.DateField()
    Open = models.FloatField()
    High = models.FloatField()
    Low = models.FloatField()
    Close = models.FloatField()
    Shares_Traded = models.IntegerField()
    Turnover_Rs_Cr = models.FloatField()

f = open("W:\Dataworkz\Dataworkztest\Datafilter\data.json","r")
json_string = f.read()
f.close()

data = json.loads(json_string)

items = []
month={'Jan':'01',"Feb":'02',"Mar":'03',"Apr":'04',"May":'05',"Jun":'06',"Jul":'07',"Aug":'08',"Sep":'09',"Oct":'10',"Nov":'11',"Dec":'12'}
for stock in data:
    d = stock["Date"][:2]
    m = stock["Date"][3:6]
    y = stock["Date"][7:]
    dt=y+"-"+month[m]+"-"+d
    s = Stock(Date = dt,
    Open = stock["Open"],
    High = stock["High"],
    Low = stock["Low"],
    Close = stock["Close"],
    Shares_Traded = stock["Shares Traded"],
    Turnover_Rs_Cr = stock["Turnover (Rs. Cr)"])
    s.save()