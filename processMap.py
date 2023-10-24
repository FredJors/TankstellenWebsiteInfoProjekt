import folium
import webbrowser
import os


def create_map(lat, lng, stations, rad):
    m = folium.Map(location=[lat, lng], zoom_start=13)
    folium.Circle(
        location=(lat, lng),
        radius=rad,
        color='red',
        fill=False
    ).add_to(m)

    for n in range(len(stations)):
        folium.Marker(
            location=stations[n][0],
            popup=stations[n][1]+"\nDieselpreis\n" + str(stations[n][2]),
            icon=folium.Icon(color='blue')
        ).add_to(m)
    m.save('map.html')
    url = os.getcwd()
    webbrowser.get("Chrome").open("file://"+url+"/map.html")

        

            
