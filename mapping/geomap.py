import folium
import pandas

df = pandas.read_csv("mapping/Volcano.txt")
coordinates = df.loc[:,('LAT','LON')]

lats = list(df["LAT"])
lons = list(df["LON"])
names = list(df["NAME"])
elvs = list(df["ELEV"])

def color_def(elv):
    if elv >=3000:
        return 'red'
    elif elv >=2000 and elv < 3000:
        return 'blue'
    else:
        return 'green'

fg = folium.FeatureGroup(name = "VolcanoMap")

map = folium.Map(location = [38, -99], zoom_start=4, tiles = "Stamen Terrain")
for lat, lon, name, elv in zip(lats, lons, names, elvs):
    #print(coordinate[0])
    fg.add_child(folium.Marker(location = [lat, lon], popup=name, icon=folium.Icon(color = color_def(elv))))
fg.add_child(folium.GeoJson(data = open("mapping/world.json", mode='r', encoding= 'utf-8-sig').read(), 
style_function=lambda color: {'fillcolor': 'green' if color['properties']['POP2005'] <10000000 
else 'orange' if 10000000 <= color['properties']['POP2005'] <20000000 else 'red'}))
map.add_child(fg)

map.add_child(folium.LayerControl())
map.save("map1.html")