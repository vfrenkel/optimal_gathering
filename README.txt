Overview:

This is a simple program that uses google's geocoding api to calculate an optimal gathering location for many participant zipcodes. 
Each zip code's latitude and longitude is retrieved from the api, then averaged, then the average lat/lon is submitted to google's geocoding api to find the
location's address.


Setup instructions (tested on a linux system, should work for others without much modification):

1. untar the python-geocoder library by running:
   tar -zxf python-geocoder-0.2.tar.gz

2. enter the python-geocoder-0.2 directory.

3. run the setup python script to build, then install the library.
   python setup.py build
   python setup.py install (you should probably use root for this)

4. go back up one directory, then go into the src directory.

5. populate ZIPCODES.txt with the zipcodes you actually want to use (use same format, one zip code per line).

6. run DoomsdayDevice.py using python:
   python DoomsdayDevice.py

7. check the result it spits out on the map, see if it's reasonable.
