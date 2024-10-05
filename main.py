import requests
import tkinter
from tkinter import messagebox

window=tkinter.Tk()
window.title("Hava Durumu")
window.config(bg="lightblue",padx=30,pady=30)
window.minsize(width=400,height=500)

def get_weather():
    api_key = "5a342235b32428319b96a27f54ad8b5b"
    city = sehir_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:

        response = requests.get(url)
        weather_data = response.json()

        if response.status_code == 200:
            name_label.config(text=f"Şehir: {weather_data["name"]}")
            temp_label.config(text=f"Sıcaklık: {weather_data['main']['temp']}°C")
            feel_label.config(text=f"Hissedilen Sıcaklık: {weather_data['main']['feels_like']}°C")
            humidity_label.config(text=f"Nem: {weather_data['main']['humidity']}%")
            weather_label.config(text=f"Hava Durumu: {weather_data['weather'][0]['description']}")
        else:
            messagebox.showerror("Hata","Şehir bulunamadı.")
    except Exception as e:
        messagebox.showerror("Hata",f"Veri alınamadı. Hata : {e}")

#şehir girişi
sehir_label=tkinter.Label(text="Şehrinizi Giriniz: ",pady=5,bg="lightblue")
sehir_label.pack()

sehir_entry=tkinter.Entry()
sehir_entry.pack()

name_label=tkinter.Label(text="Şehir: ",bg="lightblue")
name_label.pack()

temp_label=tkinter.Label(text="Sıcaklık: ",bg="lightblue")
temp_label.pack()

feel_label=tkinter.Label(text="Hissedilen Sıcaklık: ",bg="lightblue")
feel_label.pack()

humidity_label=tkinter.Label(text="Nem: ",bg="lightblue")
humidity_label.pack()

weather_label=tkinter.Label(text="Hava Durumu: ",bg="lightblue")
weather_label.pack()

get_weather_button=tkinter.Button(text="Hava Durumunu Getir",command=get_weather,bd=0,highlightthickness=0)
get_weather_button.pack()



window.mainloop()


