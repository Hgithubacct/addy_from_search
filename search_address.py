import certifi
import ssl
import geopy.geocoders
def address_from_query(query,user):
    '''
    args:
        query: string of what to look up address for
        user: arbitrary user value to represent who is pining the server
        
    returns:
    location: geolocation object address of the search result'''
    
    ctx = ssl.create_default_context(cafile=certifi.where()) 
    geopy.geocoders.options.default_ssl_context = ctx                                                       

    geolocator = geopy.geocoders.Nominatim(user_agent=user)
    location = geolocator.geocode(query)  
    return location                                                   
