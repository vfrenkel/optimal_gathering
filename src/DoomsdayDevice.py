from geocode.google import GoogleGeocoderClient
from decimal import *
from time import sleep

geocoder = GoogleGeocoderClient(False)

zipcode_file = open("ZIPCODES.txt")
zipcodes = zipcode_file.readlines()

print zipcodes

# will hold tuples of latitude/longitudes
latlongs = []
for parti_zip in zipcodes:
    if parti_zip != '\n':
        result = geocoder.geocode(parti_zip)
        if result.data["results"] != []: # this shouldn't happen unless we hit a rate limit and google killed the request.
            print result.get_location()
            print str(result.get_formatted_address()) + "\n"
            loc = result.get_location()
    
            latlongs.append(loc)
    
    # we sleep between requests so google doesn't go ape-shit on us for
    # blasting them with requests too fast.
    # SERIOUSLY, DO NOT REMOVE, YOU MIGHT GET BLOCKED.
    sleep(0.1)

# sum up location coordinates and count how many there are
num_zips = 0
sum_loc = [Decimal('0.0'), Decimal('0.0')]
for loc in latlongs:
    sum_loc[0] += loc[0]
    sum_loc[1] += loc[1]
    num_zips += 1

# take the average of the coordinates
ave_loc = (sum_loc[0]/num_zips, sum_loc[1]/num_zips)

print "read " + str(num_zips) + " locations"
print "average lat/long coordinate: " + str(ave_loc)

# perform the reverse lookup to find the location defined by the 
# latitude and longitude.
latlon_query = str(ave_loc[0]) + ", " + str(ave_loc[1])
com_venue = geocoder.geocode(latlon_query)

print "\n\nDRUM ROLL PLEASE, the optimal location for all parties is:"
print com_venue.get_formatted_address()

