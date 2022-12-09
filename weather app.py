import tkinter as tk
from PIL import Image,ImageTk
import requests

root=tk.Tk()
root.title("Weather Application")
root.geometry("1920x1080")

#key 41e765b655575f9172c04acce0a7f783
# api-- https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

def format_response(weather):
    try:
        city=weather['name']
        condition=weather['weather'][0]['description']
        temp=weather['main']['temp']
        final_str='City:%s\nCondition:%s\nTemperature:%s'%(city,condition,temp)
    except:
        final_str='There was problem retrieving information'
    return final_str
def get_weather(city):
    weather_key='41e765b655575f9172c04acce0a7f783'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'APPID':weather_key,'q':city,'units':'imperial'}
    response=requests.get(url,params)
    #print(response.json())
    weather=response.json()
    print(weather['name'])
    print(weather['weather'][0]['description'])
    print(weather['main']['temp'])

    result['text']=format_response(response.json())
    icon_name=weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size=int(frame_two.winfo_height()*0.25)
    img=ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size,size)))
    weather_icon.delete('all')
    weather_icon.create_image(0,0,anchor='nw',image=img)
    weather_icon.image=img


img=Image.open('weather.jpg')
img=img.resize((1920,1080),Image.Resampling.LANCZOS)
img_photo = ImageTk.PhotoImage(img)

bg_lbl=tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=1920,height=1080)

heading=tk.Label(bg_lbl,text="Earth including over 200,000 cities",fg='red',bg='sky blue',font=('times new roman',25,'bold'))
heading.place(x=40,y=18)

frame_one=tk.Frame(bg_lbl,bg="lightblue",bd=5)
frame_one.place(x=40,y=90,width=600,height=50)

txt_box=tk.Entry(frame_one,font=('times new roman',25),width=20)
txt_box.grid(row=0,column=0,sticky='W')

btn=tk.Button(frame_one,text='Get Weather',fg='darkgreen',font=('times new roman',16,'bold'),command=lambda: get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx='100')

frame_two=tk.Frame(bg_lbl,bg="lightblue",bd=5)
frame_two.place(x=550,y=230,width=700,height=300)

result=tk.Label(frame_two,font=40,bg='white',justify='left',anchor='nw')
result.place(relwidth=1,relheight=1)

weather_icon=tk.Canvas(result,bg='white',bd=0,highlightthickness=0)
weather_icon.place(relx=.75,rely=0,relwidth=1,relheight=0.5)
root.mainloop()