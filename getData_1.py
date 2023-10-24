import requests


class WebData:
    def __init__(self):
        pass

    def get_coords(self, address):
        api_key = "16b9a37eacc14ca89c76d252183c872a"
        url = f"https://api.opencagedata.com/geocode/v1/json?q={address}&key={api_key}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if len(data['results']) > 0:
                lat = data['results'][0]['geometry']['lat']
                lng = data['results'][0]['geometry']['lng']
                return lat, lng
            else:
                print("No results found.")
        else:
            print("Error connecting to API.")

    def get_stations(self, lat, lng, rad):
        stations = []
        url = f'https://creativecommons.tankerkoenig.de/json/list.php?lat={lat}&lng={lng}&rad={rad}' \
              f'&sort=price&type=diesel&apikey=ad86c79a-4d2f-5e0e-3694-1f2a508bd6d6'
        response = requests.get(url)
        data = response.json()

        for station in data['stations']:
            if station["isOpen"]:
                status = "geöffnet"
            else:
                status = "geschlossen"
            stations.append([[station['lat'], station['lng']], station['name'], station['price']])
            print(f"{station['name']} ({station['brand']}) in {station['place']} hat einen Dieselpreis von {station['price']} Euro und ist {status}.")
        return stations


