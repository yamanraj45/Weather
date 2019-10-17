import tkinter as tk
import requests

window = tk.Tk()
window.title("Weather")

# b09f4162a554527bc93966f0b5e24d93
# API addres : api.openweathermap.org/data/2.5/forecast?q=London,us&mode=xml


def get_weather(city, frame):
    weather_key = 'b09f4162a554527bc93966f0b5e24d93'
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    name = weather['name']
    desc = weather['weather'][0]['description']
    temp = weather['main']['temp']
    for child in frame.winfo_children():
        child.destroy()
    x = tk.Label(frame, text=name)
    x.pack()
    x = tk.Label(frame, text=desc)
    x.pack()
    x = tk.Label(frame, text=temp)
    x.pack()


window.geometry("700x800")


# background_image= tk.PhotoImage(file="United.png")
# background_label=tk.Label(window,image=background_image)
# background_label.place(relwidth=1,relheight=1)


frame = tk.Frame(window, bg="#80c1fe", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

Entry1 = tk.Entry(frame, bg="grey")
Entry1.place(relheight=1, relwidth=0.65)
lower_frame = tk.Frame(window, bg="#80c1fe", bd=15)
lower_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.6, anchor='n')
button1 = tk.Button(frame, text="Get Weather", font=40,
                    command=lambda: get_weather(Entry1.get(), lower_frame))
button1.place(relx=0.7, relheight=1, relwidth=0.3)


window.mainloop()
