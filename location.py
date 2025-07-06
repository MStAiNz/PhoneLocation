#on the  terminal, type "pip install phonenumbers"
import phonenumbers
import folium
from phoneNumber import number
from phonenumbers import geocoder
from phonenumbers import carrier

Key = "cf49966fc6eb4bbab7e30f9eb42b4afe"

myNumber = phonenumbers.parse(number)
theLocation = geocoder.description_for_number(myNumber, "en")
print(theLocation)

serviceProvider = phonenumbers.parse(number)
print(carrier.name_for_number(serviceProvider, "en"))

#longitude and latitude
#on the  terminal, type "pip install opencage"
from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)

query = str(theLocation)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)

folium.Marker([lat, lng], popup = theLocation).add_to((myMap))

#save Map in html file to view on browswer
myMap.save("theLocation.html")