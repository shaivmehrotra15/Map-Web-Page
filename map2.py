import folium
import pandas
 
data = pandas.read_csv("Webmap_datasources/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])
stat = list(data["STATUS"])
 
html = """
Volcano name:
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank",
        style="text-decoration: none">%s</a><br>
Height: %s m
<br>
Status: %s
"""
 
map = folium.Map(location=[38.58, -99.09], zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name = "My Map")
 
for lt, ln, el, name, st in zip(lat, lon, elev, name, stat):
    iframe = folium.IFrame(html=html % (name, name, el, st), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = "green")))
 
map.add_child(fg)
map.save("Map_html_popup_advanced.html")