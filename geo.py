import webbrowser
from geopy.geocoders import Nominatim

def get_coordinates(location):
    geolocator = Nominatim(user_agent="geo_locator")
    location = geolocator.geocode(location)
    if location:
        return location.latitude, location.longitude
    else:
        return None

def open_google_maps(latitude, longitude):
    if latitude is not None and longitude is not None:
        url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
        webbrowser.open_new_tab(url)
    else:
        print("Coordinates not found for the given location.")

def geo_in_map():
    location = input("Enter Location: ")
    coordinates = get_coordinates(location)
    print(coordinates)
    open_google_maps(*coordinates)

if __name__ == "__main__":
    geo_in_map()

