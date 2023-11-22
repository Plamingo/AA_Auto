#import streamlit as st
import datetime 

d = datetime.date(2016,7,24)
tday = datetime.date.today()

print(d)
print(tday.day)

print(tday.weekday()) #monday = 0
print(tday.isoweekday()) #monday = 1

tdelta = datetime.timedelta(days=7)
print(tday)
print(tday - tdelta)

#date2= date1 + tdelta 

bday = datetime.date(2024,2,15)
till_bday = bday - tday
print(bday)
print(till_bday.total_seconds())


#t = datetime.time(9,30,45,100000)
dt = datetime.datetime(2016,7,26,12,30,45,100000)
#tdelta = datetime.timedelta(days=7)
#tdelta = datetime.timedelta(hours=12)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print (dt_today)
print (dt_now)
print (dt_utcnow)


