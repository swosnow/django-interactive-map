from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="mapaguapi")

a = 'Capim,  Guapimirim - RJ'
location = geolocator.geocode(a)
print(location.address)

print((location.latitude, location.longitude))

print(location.raw)

