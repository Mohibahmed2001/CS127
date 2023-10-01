#Mohib AHmed
#June 27 2023
#mohib.ahmed79@myhunter.cuny.edu
#Create a map of nyc with a marker on hunter

#Import the folium package for making maps
import folium
import pandas as pd
namefile = input("Please give me nameof the file")
accident = pd.read_csv(namefile)
mapNYC = folium.Map(location=[40.75, -74.125], zoom_start=10)
for index,row in accident.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["CRASH TIME"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapNYC)
outputfile = input("give output file")
mapNYC.save(outfile=outputfile)
