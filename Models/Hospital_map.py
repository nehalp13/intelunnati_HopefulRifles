import folium
import pandas as pd

# Creates a Leaflet map centered around India
map = folium.Map(location=[22.309425, 72.136230], zoom_start=7)

# Define custom marker icons
icon_image1 = 'marker1.png'  # Path to first custom marker image
icon_size1 = (20, 20)  # Size of the first custom marker

icon_image2 = 'marker2.png'  # Path to second custom marker image
icon_size2 = (25, 25)  # Size of the second custom marker

# Functions to add markers from CSV data
def add_markers_from_csv(csv_file, icon_image, icon_size):
    # Loads data from a CSV file
    accident_data = pd.read_csv(csv_file)

    # Adds markers to the map
    for index, row in accident_data.iterrows():
        lat = row['Latitude']
        lon = row['Longitude']
        location = row['Location']
        description = row['Description']
    
        # Creates a custom icon from image file
        custom_icon = folium.CustomIcon(icon_image, icon_size=icon_size)
    
        # Creates a marker with the custom icon for each location
        marker = folium.Marker([lat, lon], icon=custom_icon, popup=f'<strong>{location}</strong><br>{description}')
    
        # Adds the marker to the map
        marker.add_to(map)

# Add markers from first CSV file with first custom marker
add_markers_from_csv('blackspot_data.csv', icon_image1, icon_size1)

# Add markers from second CSV file with second custom marker
add_markers_from_csv('hospital_data.csv', icon_image2, icon_size2)

# Saves the map to an HTML file
map.save('Hospital_map.html')