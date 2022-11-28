

import city_country_csv_reader

import networkx as nx
from locations import City, Country
from trip import Trip
from vehicles import Vehicle, create_example_vehicles


def find_shortest_path(vehicle: Vehicle, from_city: City, to_city: City) -> Trip:
    
    """
    Returns a shortest path between two cities for a given vehicle,
    or None if there is no path.
    """
    
#     city_country_csv_reader.create_cities_countries_from_CSV("worldcities_truncated.csv")                             
 
    G  = nx.Graph()
    
    for i in City.cities.values():

        G.add_node(i)
        for j in City.cities.values():
            if j != i:
                G.add_edge(i,j,weight = vehicle.compute_travel_time(i,j) )                       


    
    paths = nx.shortest_path(G,from_city ,to_city , weight="weight" , method='dijkstra')                   

    if len(paths) > 0 :
        for m in range(len(paths)):
            if m ==0:
                trip = Trip(paths[m])
            else:
                trip.add_next_city(paths[m])
        return trip
    else:
        return None
                                                                                                                                                                            

if __name__ == "__main__":
    city_country_csv_reader.create_cities_countries_from_CSV("worldcities_truncated.csv")

    vehicles = create_example_vehicles()

    australia = Country.countries["Australia"]
    melbourne = australia.get_city("Melbourne")
    japan = Country.countries["Japan"]
    tokyo = japan.get_city("Tokyo")

    for vehicle in vehicles:
        print("The shortest path for {} from {} to {} is {}".format(vehicle, melbourne, tokyo, find_shortest_path(vehicle, melbourne, tokyo)))





