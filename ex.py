import pandas as pd
from geopy import distance

airports = pd.read_csv('airports.csv')
routes = pd.read_csv('routes.csv')

def filter(airports, routes):
  filtered = []

  for ind in routes.index:
    source_airport_id = routes['Source airport ID'][ind]
    dest_airport_id = routes['Destination airport ID'][ind]

    source_airport_name = routes['Source airport'][ind]
    dest_airport_name = routes['Destination airport'][ind]

    source_airport = airports.loc[airports['IATA'] == source_airport_name]
    dest_airport = airports.loc[airports['IATA'] == dest_airport_name]

    if(
      'N' in list(source_airport_id)
    ):
      print(ind, 'no ID given to source airport in routes')
      continue
    
    if(
      'N' in list(dest_airport_id)
    ):
      print(ind, 'no ID given to destination airport in routes')
      continue
    
    if(
      len(source_airport) == 0
    ):
      print(ind, 'couldn\'t find source airport with such name', source_airport_name)
      continue
    
    if(
      len(dest_airport) == 0
    ):
      print(ind, 'couldn\'t find destination airport with such name', dest_airport_name)
      continue

    if(
      int(source_airport['Airport ID']) != int(source_airport_id) or
      int(dest_airport['Airport ID']) != int(dest_airport_id)
    ):
      print(ind, 'The ids do not match')
      continue

    filtered.append([routes['Source airport ID'][ind], routes['Destination airport ID'][ind]])

  return pd.DataFrame(filtered, columns=['source_ID', 'destination_ID'])

def routes_in_europe(routes, airports):
  european_routes = []

  for ind in routes.index:
    source_airport_id = routes['source_ID'][ind]
    dest_airport_id = routes['destination_ID'][ind]

    source_airport = airports.loc[airports['Airport ID'] == int(source_airport_id)]
    dest_airport = airports.loc[airports['Airport ID'] == int(dest_airport_id)]

    if(
      'Europe' in source_airport['Tz database time zone'].to_string() and
      'Europe' in dest_airport['Tz database time zone'].to_string()
    ):
      print('+++')
      european_routes.append([source_airport_id, dest_airport_id])
  
  return pd.DataFrame(european_routes, columns=['source_ID', 'destination_ID'])


filtered_routes = filter(airports, routes)

european_routes = routes_in_europe(filtered_routes, airports)

print(european_routes)

coords_1 = (52.2296756, 21.0122287)
coords_2 = (52.406374, 16.9251681)

print(distance.distance(coords_1, coords_2).km)