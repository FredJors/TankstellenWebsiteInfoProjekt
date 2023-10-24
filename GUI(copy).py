import tkinter as tk
import webbrowser


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import processMap
import getData_1

from PIL import Image, ImageTk

webbrowser.open_new('map.html')
def button_map_clicked():
    label.config(text="opening map...")
    lat, lng = data.get_coords(get_value(address, False))
    stations = data.get_stations(lat, lng, get_value(rad, False))
    processMap.create_map(lat, lng, stations, int(get_value(rad, False)) * 1000)


def get_value(entry, delete):
    if delete is True:
        entry.delete("0", "end")
    return entry.get()


data = getData_1.WebData()

master = tk.Tk()
master.title("FuelHelper 1.0.0")

width = master.winfo_screenwidth()
height = master.winfo_screenheight()
master.geometry("%dx%d" % (width, height))

image = Image.open("Tankstelle.jpeg")

# resize the image to fit the screen
image = image.resize((width, height), Image.LANCZOS)

# convert the image to Tkinter format
bg_image = ImageTk.PhotoImage(image)

# create a label with the background image
bg_label = tk.Label(master, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

label = tk.Label(master, text="Welcome to FuelHelper!", font=("Arial",18))
label.grid(row=1, column=2, columnspan= 3)

address_label = tk.Label(master, text="Ort:", font=("Arial",18))
address_label.grid(row=2, column=1, columnspan=3)

address = tk.Entry(master, width=30)
address.insert("0", "Berlin")   #statt Berlin in Datenbank gespeicherter Ort
address.grid(row=2, column=2, columnspan=3)

rad_label = tk.Label(master, text="Radius (km):", font=("Arial",18))
rad_label.grid(row=3, column=1, columnspan=3)

rad = tk.Entry(master, width=30)
rad.insert("0", "20")
rad.grid(row=3, column=2, columnspan=3)

fuel_type_label = tk.Label(master, text="Kraftstoffart:", font=("Arial",18))
fuel_type_label.grid(row=4, column=1, columnspan=3)

fuel_type = tk.StringVar(value="Super E10")
fuel_type_dropdown = tk.OptionMenu(master, fuel_type, "Super E10", "Super E5", "Diesel")
fuel_type_dropdown.grid(row=4, column=2, columnspan=3)

button_map = tk.Button(master, text="Click me to show map!", font=("Arial",18), command=button_map_clicked)
button_map.grid(row=6, column=2, columnspan=3)

# easy diagram
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(14.5, 4))
axs[0].plot(['A', 'B', 'C', 'D'], [10, 20, 30, 40])
axs[1].plot(['X', 'Y', 'Z'], [5, 15, 25])
axs[2].plot(['M', 'N', 'O'], [8, 24, 16])

for i, ax in enumerate(axs):
    ax.set_title(f"Diagramm {i+1}")
    ax.set_xlabel("Zeit")
    ax.set_ylabel("Preis")
    ax.grid(True)

canvas = FigureCanvasTkAgg(fig, master=master)
canvas.draw()

canvas.get_tk_widget().grid(row=10, column=1, columnspan=5)


# dropdown menu for time range selection
def update_graphs():
    # update graphs based on selected fuel type and time range
    fuel_type_selected = fuel_type.get()
    time_range_selected = time_range.get()
    data_list = []

    # get data for selected fuel type and time range
    if fuel_type_selected == "Super E10":
        if time_range_selected == "letzte 24h":
            data_list = [1, 2, 3, 4]  # replace with actual data

        elif time_range_selected == "letzte Woche":
            data_list = [2, 3, 4, 5]  # replace with actual data
        elif time_range_selected == "letzten Monat":
            data_list = [3, 4, 5, 6]  # replace with actual data
    elif fuel_type_selected == "Super E5":
        if time_range_selected == "letzte 24h":
            data_list = [4, 3, 2, 1]  # replace with actual data
        elif time_range_selected == "letzte Woche":
            data_list = [5, 4, 3, 2]  # replace with actual data
        elif time_range_selected == "letzten Monat":
            data_list = [6, 5, 4, 3]  # replace with actual data
    elif fuel_type_selected == "Diesel":
        if time_range_selected == "letzte 24h":
            data_list = [7, 8, 9, 10]  # replace with actual data
        elif time_range_selected == "letzte Woche":
            data_list = [8, 9, 10, 11]  # replace with actual data
        elif time_range_selected == "letzten Monat":
            data_list = [9, 10, 11, 12]  # replace with actual data

    # update graphs with new data
    for i, ax in enumerate(axs):
        ax.clear()
        ax.plot(['A', 'B', 'C', 'D'], data_list)
        ax.set_title(f"Diagramm {i+1}")
        ax.set_xlabel("X-Achse")
        ax.set_ylabel("Y-Achse")
        ax.grid(True)
    canvas.draw()


# dropdown menu for time range selection
time_range_label = tk.Label(master, text="Zeitraum:", font=("Arial",18))
time_range_label.grid(row=5, column=1, columnspan=3)

time_range = tk.StringVar(value="letzte 24h")
time_range_dropdown = tk.OptionMenu(master, time_range, "letzte 24h", "letzte Woche", "letzten Monat")
time_range_dropdown.grid(row=5, column=2, columnspan=3)


# button to update graphs
update_button = tk.Button(master, text="Aktualisieren", font=("Arial",15), command=update_graphs)
update_button.grid(row=11, column=2, columnspan=3)

master.mainloop()
