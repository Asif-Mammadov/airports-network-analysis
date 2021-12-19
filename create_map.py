import folium
from geopy.geocoders import Nominatim

def create_map(airports, file_name):
    geolocator = Nominatim(user_agent = 'RusAsMar')
    m = folium.Map(location = [47.3441, 0.6848], zoom_start = 5)    

    for ind in airports.index:
        tooltip = f"{ind}"
        folium.Marker([airports['Latitude'][ind], airports['Longitude'][ind]], popup=f"<strong>{ind}</strong>", tooltip=tooltip, icon=folium.Icon(color = "blue")).add_to(m)
    
    m.save(file_name)
