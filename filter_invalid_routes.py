import pandas as pd
from geopy import distance

# arguments are the dataframes
# example of usage :
# print(filter(pd.read_csv('airports.csv'), pd.read_csv('routes.csv')))
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

    filtered.append([
        routes['Source airport ID'][ind],
        routes['Destination airport ID'][ind],
        source_airport['Latitude'].to_string().split(' ')[-1],
        source_airport['Longitude'].to_string().split(' ')[-1],
        dest_airport['Latitude'].to_string().split(' ')[-1],
        dest_airport['Longitude'].to_string().split(' ')[-1],
        distance.distance(
            (float(source_airport['Latitude'].to_string().split(' ')[-1]), float(source_airport['Longitude'].to_string().split(' ')[-1])),
            (float(dest_airport['Latitude'].to_string().split(' ')[-1]), float(dest_airport['Longitude'].to_string().split(' ')[-1]))
        ).km]
    )

  return pd.DataFrame(filtered, columns=['source_ID', 'destination_ID', 'source_latitude', 'source_longtitude', 'dest_latitude', 'dest_longtitude', 'distance_km'])

filtered_routes = filter(pd.read_csv('airports.csv'), pd.read_csv('routes.csv'))

print(filtered_routes)