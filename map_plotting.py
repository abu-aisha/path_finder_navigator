
import city_country_csv_reader
from locations import create_example_countries_and_cities
from trip import Trip, create_example_trips
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

def plot_trip(trip: Trip, projection = 'robin', line_width=2, colour='b') -> None:
    """
    Plots a trip on a map and writes it to a file.
    Ensures a size of at least 50 degrees in each direction.
    Ensures the cities are not on the edge of the map by padding by 5 degrees.
    The name of the file is map_city1_city2_city3_..._cityX.png.
    """

    
    m = Basemap(projection=projection,lon_0=9)
    name_lst = []
    cities = trip.cities
    longs = []
    lats = []
    for city in cities:
        name_lst.append(city.name)
        xpt, ypt = m(float(city.longitude), float(city.latitude))
        longs.append(xpt)
        lats.append(ypt)
    
    m.drawcoastlines()
    name = f"{'_'.join(name_lst)}.png"
    m.plot(longs, lats, color=colour, linewidth=line_width)#, label='Flight 98')
    plt.savefig(name)
    


if __name__ == "__main__":
    city_country_csv_reader.create_cities_countries_from_CSV("worldcities_truncated.csv")

    create_example_countries_and_cities()

    trips = create_example_trips()

    for trip in trips:
        plot_trip(trip)









