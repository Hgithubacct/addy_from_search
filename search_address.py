import certifi
import ssl
import geopy.geocoders

ctx = ssl.create_default_context(cafile=certifi.where()) 
geopy.geocoders.options.default_ssl_context = ctx                                                       

geolocator = geopy.geocoders.Nominatim(user_agent="henry")
location = geolocator.geocode("sushi in austin")                                                     
