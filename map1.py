import folium
import pandas

data = pandas.read_csv("Webmap_datasources/Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 2500 > elevation >= 1000 :
        return 'darkpurple'
    else :
        return 'red'    

html = """<h4>Volcano information:</h4>
Height: %s m"""

map = folium.Map(location=[40, -115],zoom_start=6, tiles = "Stamen Terrain")

fg1=folium.FeatureGroup(name="volcanoes")
fg2=folium.FeatureGroup(name="population")

for la,ln,el in zip(lat,lon,elev) :
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)

    #fg.add_child(folium.Marker(location=[la, ln],popup=folium.Popup(str(el)+" m",parse_html=True) ,icon = folium.Icon(color='darkpurple')))

    fg1.add_child(folium.Marker(location=[la, ln],popup=folium.Popup(iframe) ,icon = folium.Icon(color=color_producer(el))))

fg2.add_child(folium.GeoJson(data = open('Webmap_datasources/world.json','r',encoding='utf-8-sig',).read(), style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))

map.add_child(fg1)
map.add_child(fg2)

map.add_child(folium.LayerControl())

map.save("map1.html")

#use dir(folium) for list of functions and help(folium.functionName) for info about the function