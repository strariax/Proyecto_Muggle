import folium
import os

# Custom icon path
custom_icon_path = "./static/tree.png"

# Create a map centered at a specific location
map_center = [-25.30794548607119, -57.60156947570091]
mapPeople = folium.Map(location=map_center, zoom_start=12)

# Define locations
locations = [
    {"name": "Quebracho", "coordinates": [-25.30794548607119, -57.60156947570091]},
    {"name": "Yvoty", "coordinates": [-25.28976557704737, -57.58262309056482]},
    {"name": "Palo Santo", "coordinates": [-25.324391874005, -57.58511437253675]},
    {"name": "Guayacán", "coordinates": [-25.300190732059814, -57.599930545572164]},
    {"name": "Timbó", "coordinates": [-25.297944594982464, -57.55630568731381]},
    {"name": "Santa Lucía", "coordinates": [-25.33623546676696, -57.60908323247559]},
    {"name": "Barrio Pirayú", "coordinates": [-25.273671205165908, -57.47118823830609]},
    {"name": "Marambure", "coordinates": [-25.267820531492355, -57.47022259197445]},
    {"name": "Zona Norte", "coordinates": [-25.320236503010594, -57.531550210057894]},
    {"name": "Zona Sur", "coordinates": [-25.340694034103063, -57.56040188164488]},
    {"name": "San Antonio", "coordinates": [-25.35440538852731, -57.5107405279881]}
]

# Define tree names
tree_names = [
    "Quebracho", "Yvoty", "Palo Santo", "Guayacán", "Timbó",
    "Santa Lucía", "Barrio Pirayú", "Marambure", "Zona Norte",
    "Zona Sur", "San Antonio"
]

# Define volunteer names
volunteer_names = [
    "Alejandro", "Sofia", "Mateo", "Isabella", "Gabriel",
    "Valentina", "Diego", "Camila", "Luis", "Elena", "Carlos"
]

# Define dates
dates = [
    "11/01/23", "11/07/23", "11/15/23", "11/21/23", "11/28/23",
    "12/03/23", "12/09/23", "12/17/23", "12/22/23", "12/27/23", "12/31/23"
]

# Folder path for images
image_folder = "./static/"

# Iterate through locations and add markers to the map
for i, location in enumerate(locations):
    # Determine the image file path
    image_file = f"{image_folder}person{i + 1}.png"

    popup_content = f"""
        <div style="width:200px;">
            <strong>Coordinate</strong><br>
            Tipo de Árbol: {tree_names[i]}<br>
            Fecha: {dates[i]}<br>
            Plantó: {volunteer_names[i]}<br>
            <img src="{image_file}" alt="{volunteer_names[i]}" style="width:100%;">
        </div>
    """
    folium.Marker(
        location["coordinates"],
        popup=folium.Popup(popup_content),
        icon=folium.CustomIcon(icon_image=custom_icon_path, icon_size=(30, 30))
    ).add_to(mapPeople)

# Save the map to an HTML file
mapPeople.save("mapita_with_people_icon.html")
