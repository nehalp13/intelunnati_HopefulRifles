import folium
import pandas as pd

# Loads accident data from CSV file
accident_data = pd.read_csv('blackspot_data.csv')

# Creates a Leaflet map centered around India
map = folium.Map(location=[22.309425, 72.136230], zoom_start=7)

# Add accident markers to the map
for index, row in accident_data.iterrows():
    lat = row['Latitude']
    lon = row['Longitude']
    location = row['Location']
    description = row['Description']
    
    # Creates a custom icon from an image file
    icon_image = 'marker1.png'  # Custom marker image file
    icon_size = (32, 32)  # Size of the custom marker
    custom_icon = folium.CustomIcon(icon_image, icon_size=icon_size)
    
    # Creates a marker with the custom icon for each accident location
    marker = folium.Marker([lat, lon], icon=custom_icon, popup=f'<strong>{location}</strong><br>{description}')
    
    # Adds the marker to the map
    marker.add_to(map)

# Saves the map to an HTML file
map.save('Blackspot_map.html')