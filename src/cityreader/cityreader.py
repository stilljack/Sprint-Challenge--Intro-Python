# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
import csv
import textwrap
import decimal


class City:
  #name:city lat:state_name, lon:['county_name', 'lat', 'lng', 'population', 'density', 'timezone', 'zips']

  cityName=""
  stateName = ""
  countyName =""
  lat = 0.1
  lon = 0.1
  population = 0.1
  density = 0.1
  timeZone ="pst"
  zips = []
  def __init__(self,cityName,lat,lon,stateName="",countyName="",population="",density="",timeZone="",zips:list=""):
    self.cityName=cityName #0
    self.stateName=stateName #1
    self.countyName=countyName #2
    self.lat=float(lat) #3
    self.lon=float(lon) #4
    self.population=population
    self.density=density
    self.timeZone=timeZone
    self.zips=zips

  def __str__(self):
    zipJoin = ', '.join(self.zips)
    return (f"""
{self.cityName},{self.countyName} county,{self.stateName} 
LatLng: {self.lat}, {self.lon}
Population: {self.population}
Density: {self.density}
Time Zone: {self.timeZone}
Zip Codes: {textwrap.fill(zipJoin,80)}""")

cities = []

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
  #name:city lat:state_name, lon:['county_name', 'lat', 'lng', 'population', 'density', 'timezone', 'zips']
  with open('cities.csv') as csvf:
    next(csvf)
    csvReader = csv.reader(csvf)

    for row in csvReader:
      zipsSplit = row[8].split(" ")
      #prob a better way to do this
      lat = row[3]
      lon = row[4]
      newCity = City(row[0],lat,lon, row[1], row[2],row[5],row[6],row[7],zipsSplit)
      cities.append(newCity)

  return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
  print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user
latEntryCheck =True
lonEntryCheck =True
def latInput(current):
  lat = input(f"input lattitude {current}")
  try:
    val = float(lat)
    #print(f"{val} is a float")
    global latEntryCheck
    latEntryCheck=False
    return val
  except ValueError:
    print("That's not an float!")
    latInput()

def lonInput(current):
  lon = input(f"input longitude {current}")
  try:
    val = float(lon)
    #print(f"{val} is a float")
    global lonEntryCheck
    lonEntryCheck=False
    return val
  except ValueError:
    print("That's not an float!")
    lonInput()

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []

  # TODO Ensure that the lat and lon valuse are all floats
  # Go through each city and check to see if it falls within
  # the specified coordinates.
  higherLat:float
  lowerLat:float
  higherLon:float
  lowerLon:float
  if lat1>lat2:
    higherLat=lat1
    lowerLat=lat2
    higherLon=lon1
    lowerLon=lon2
  else:
    higherLat=lat2
    lowerLat=lat1
    higherLon=lon2
    lowerLon=lon1

  for city in cities:
    if higherLat > city.lat and higherLon > city.lon:
      if lowerLat < city.lat and lowerLon < city.lon:
        within.append(city)
  return within

  #count=-1
  #for i in zipsSplit:
  #count+=1
  #print(f"i = {count} and zipsplit[i] {i}")

def comboInput():
  combo = input(f"input lat/lon range as 4 floats delinieated by spaces i.e. 30 100 40 110\n~")
  split = combo.split(" ")
  try:
    lat1 = float(split[0])
    lon1 = float(split[1])
    lat2 = float(split[2])
    lon2 = float(split[3])
    #print(f"{val} is a float")
    global  latEntryCheck
    latEntryCheck =False
    global lonEntryCheck
    lonEntryCheck=False
    citiesReturned= cityreader_stretch(lat1,lon1,lat2,lon2,cityreader(cities))
    return citiesReturned

  except ValueError:
    print("at one of those aint no float!")
    combo()
#while latEntryCheck or lonEntryCheck:
  #lat1 =latInput(1)
  #lon1 = lonInput(1)
  #lat2 =latInput(2)
  #lon2 = lonInput(2)
  #print(comboInput())

