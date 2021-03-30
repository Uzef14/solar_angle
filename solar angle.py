#To get the lattitude of entered city
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my_user_agent")

city = input("ENTER THE CITY NAME")


country = input("ENTER THE COUNTRY NAME")
loc = geolocator.geocode(city+','+country)
print("latitude is :-" ,loc.latitude,"\nlongtitude is:-" ,loc.longitude)
latitude=loc.latitude
import datetime

today=datetime.date.today()
intialday=datetime.date(2021 ,1, 1)
n=today-intialday
today=n.days
print("n",today)

from datetime import datetime
now=datetime.now().time()
current_time =now.strftime("%H:%M")
newcurrent_time=current_time.replace(":","")

print("TIME IS",newcurrent_time)

angle=float(input("ENTER THE SLOPE ANGLE"))


w2=(1200-int(newcurrent_time))*15
print("LOCAL APPERENT TIME IS",w2**-2)


import math


d=23.45*(math.sin(math.radians(0.98*(284+today))))
print("ANGLE OF DECLINATION",d)

sin1=math.sin(math.radians(d))
sin2=math.sin(math.radians(latitude-angle))
cosd=math.cos(math.radians(d))
cosob=math.cos(math.radians(latitude-angle))
cosw1=math.cos(math.radians(w2))
Q1=((cosob*cosd*cosw1)+(sin1*sin2))
Q=math.cos((Q1))
angel=float(Q*100)
print("THE ANGLE IS",angel)















