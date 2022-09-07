import requests
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import os
from PIL import Image
import random
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[2].id)


def speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")



Api_Key = "bRwpUuFWhuTpcQrutjrigQDsTi4GQhBBJIsLAnJR"




def IssTracker():
    url = "http://api.open-notify.org/iss-now.json"

    r = requests.get(url)

    Data = r.json()

    dt = Data['timestamp']

    lat = Data['iss_position']['latitude']

    lon = Data['iss_position']['longitude']

    speak(f"Time And Date : {dt}")
    speak(f"Latitude : {lat}")
    speak(f"Longitude : {lon}")
    speak('this is the particular place')

    plt.figure(figsize=(5, 5))

    ax = plt.axes(projection=ccrs.PlateCarree())

    ax.stock_img()

    plt.scatter(float(lon), float(lat), color='blue', marker='o')

    plt.show()





def Astro(start_date,end_date):

    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_Key}"

    r = requests.get(url)

    Data = r.json()

    Total_Astro = Data['element_count']

    neo = Data['near_earth_objects']

    speak(f"Total Astroid Between {start_date} and {end_date} Is : {Total_Astro}")
    speak("Extact Data For Those Astroids Are Listed Below ")

    for body in neo[start_date]:

        id = body['id']

        name = body['name']

        absolute = body['absolute_magnitude_h']

        print(id,name,absolute)