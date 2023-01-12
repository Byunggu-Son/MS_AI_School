import requests, json
import smtplib 
import csv
import os
import folium
import asyncio 
import winsdk.windows.devices.geolocation as wdg
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 
from geopy.geocoders import Nominatim 
from dotenv import load_dotenv 
import io 
from PIL import Image
import time


start = time.time()
 
def send_alarm():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    load_dotenv()
    sender = os.getenv('USER_NAME')
    pw = os.getenv('PASSWORD')
    s.login(sender , pw)
    address = get_location()
    customers = get_customer()
    msg = MIMEText(f"*** 경고 ***\n\n현재 아래 좌표에서 드론이 관측되었습니다.\n\n {address}")
    
    msg['Subject'] = '제목 : 드론 경고 알림입니다.'
    for users in customers:
        s.sendmail(sender, users, msg.as_string())
    s.quit()
    print("E-mail Sent to All Customer")
async def getCoords():
    locator = wdg.Geolocator()
    pos = await locator.get_geoposition_async()
    return [pos.coordinate.latitude, pos.coordinate.longitude]
def getLoc():
    try:
        return asyncio.run(getCoords())
    except PermissionError:
        print("ERROR: You need to allow applications to access you location in Windows settings")
def geocoding_reverse(lat_lng_str): 
    geolocoder = Nominatim(user_agent = 'South Korea', timeout=None)
    address = geolocoder.reverse(lat_lng_str)
    return address
def get_location():
    coordinate = getLoc()
    lat = str(coordinate[0])
    lng = str(coordinate[1])
    location = lat+', '+lng
    address = geocoding_reverse(location)
    return address
def get_customer():
    data = []
    customer_data = './customer.csv'
    f = open(customer_data,'r',encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        tmpstring = ''
        tmpstring = line[0]
        data.append(tmpstring)
    f.close()
    return data
send_alarm()


# end = time.time()

# print(end-start)


address = getLoc()
print(address)

map_ = folium.Map(location=address, zoom_start=13, prefer_canvas=True, zoom_control=False,scrollWheelZoom=False, dragging=False)
marker = folium.CircleMarker(address, radius=50, color='red', fill_color='red')
marker.add_to(map_)
map_.save('mymap.html')