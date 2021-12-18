import pandas as pd

# arguments are the dataframes
# example of usage :
# print(routes_in_europe(pd.read_csv('airports.csv'), pd.read_csv('routes.csv')))
def routes_in_europe(airports, routes):
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
      european_routes.append([source_airport_id, dest_airport_id])

  return pd.DataFrame(european_routes, columns=['source_ID', 'destination_ID', 'source_latitude', 'source_longtitude', 'dest_latitude', 'dest_longtitude', 'distance_km'])