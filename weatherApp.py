from tkinter import *
from tkinter import messagebox
import requests
from datetime import datetime

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f216292e5d75bac230e58adf97a5faab'

def get_weather(city):
    # connect to api
    response = requests.get(url.format(city))
    # api to json data
    data = response.json() 
    
    if data:
        #Temps
        currentTemp = data['main']['temp']
        tempMin = data['main']['temp_min']
        tempMax = data['main']['temp_max']

        #humidity
        humidity = data['main']['humidity']

        #Wind
        windSpeed = data['wind']['speed']
        windDegree = data['wind']['deg']

        #Wind Direction(degree to cardinal)
        arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
        deg =int((windDegree/22.5)+0.5)
        cardinalDirection = (arr[(deg % 16)])

        #Description
        description = data['weather'][0]['description']

        #Sun
        sRise = data['sys']['sunrise']
        sSet = data['sys']['sunset']
        sunrise = datetime.utcfromtimestamp(sRise).strftime('%Y-%m-%d %H:%M:%S')
        sunset = datetime.utcfromtimestamp(sSet).strftime('%Y-%m-%d %H:%M:%S')

        #Icon
        icon = data['weather'][0]['icon']

        result = (currentTemp, tempMin, tempMax, humidity, windSpeed, cardinalDirection, description, sunrise, sunset, icon)
        return result

def search():
    city = city_name.get()
    weather = get_weather(city) #is the result tuple
    if weather:
        city_lbl['text'] = '{}'.format(city)

        #Icon Display
        icon['file'] = weather[9]+'.png'

        #weather with index of result#
        currentTemp_lbl['text'] = '{} °C'.format(weather[0])
        minTemp_lbl['text'] = '{} °C'.format(weather[1])
        maxTemp_lbl['text'] = '{} °C'.format(weather[2])
        humidity_lbl['text'] = '{} %'.format(weather[3])
        windSpeed_lbl['text'] = '{} km/h'.format(weather[4])
        cardDirection_lbl['text'] = '{}'.format(weather[5])
        description_lbl['text'] = '{}'.format(weather[6])
        sunrise_lbl['text'] = '{}'.format(weather[7])
        sunset_lbl['text'] = '{}'.format(weather[8])
    
###GUI###
app = Tk()
app.title('Weather App')

#get icon file, display as label 
icon = PhotoImage(file='')
weatherIcon = Label(image=icon)
weatherIcon.place(x=-60, y=-70, relwidth=1, relheight=1)

city_name = StringVar()
city_entry = Entry(app, textvariable=city_name)
city_entry.grid(column=2, row=0)

search_btn = Button(app, text='Get Weather', width=10, bg='gray', command=search)
search_btn.grid(column=2, row=1)

city_lbl = Label(app, text='', font=(15))
city_lbl.grid(column=2, row=3)

description_lbl = Label(app, text='', font=('bold', 15))
description_lbl.grid(column=1, row=5)

#Label(app, text='Current Temperature', font=('bold', 10)).grid(column=3, row=4)
currentTemp_lbl = Label(app, text='', font=('bold', 20))
currentTemp_lbl.grid(column=2, row=5)

#Label(app, text='Max Temperature', font=('bold', 10)).grid(column=2, row=6)
maxTemp_lbl = Label(app, text='', fg='red')
maxTemp_lbl.grid(column=2, row=4)

#Label(app, text='Min Temperature', font=('bold', 10)).grid(column=1, row=6)
minTemp_lbl = Label(app, text='', fg='blue')
minTemp_lbl.grid(column=2, row=6)

#simple white space
Label(app, text='').grid(column=1, row=7)

Label(app, text='Humidity', font=('bold', 10)).grid(column=1, row=8)
humidity_lbl = Label(app, text='')
humidity_lbl.grid(column=2, row=8)

Label(app, text='Wind Speed', font=('bold', 10)).grid(column=1, row=9)
windSpeed_lbl = Label(app, text='')
windSpeed_lbl.grid(column=2, row=9)

Label(app, text='Wind Direction', font=('bold', 10)).grid(column=1, row=10)
cardDirection_lbl = Label(app, text='')
cardDirection_lbl.grid(column=2, row=10)

Label(app, text='Sunrise', font=('bold', 10)).grid(column=1, row=11)
sunrise_lbl = Label(app, text='')
sunrise_lbl.grid(column=2, row=11)

Label(app, text='Sunset', font=('bold', 10)).grid(column=1, row=12)
sunset_lbl = Label(app, text='')
sunset_lbl.grid(column=2, row=12)

app.mainloop()