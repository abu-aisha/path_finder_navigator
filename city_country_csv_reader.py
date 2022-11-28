from locations import City, Country, test_example_countries_and_cities

import csv



def create_cities_countries_from_CSV(path_to_csv: str) -> None:
    """
    Reads a CSV file given its path and creates instances of City and Country for each line.
    """
    with open(path_to_csv,newline="",encoding="utf8") as f:
        reader = csv.DictReader(f)
        # ctry_lst = []
        ctry_dict_lst = []
        ctry_dict = dict()
        data_dict = {}
        x=0
        for row in reader:
            
            if row["country"] not in ctry_dict_lst:
                ctry_dict_lst.append(row["country"])
                ctry_dict[row["country"]] = row["iso3"]
                data_dict[row["country"]] = {row["city_ascii"]:[row["lat"],row["lng"],row["capital"],row["id"]]}
            else:
                data_dict[row["country"]][row["city_ascii"]] = [row["lat"],row["lng"],row["capital"],row["id"]]
    for country in data_dict:
   
        country_obj = Country(country,ctry_dict[country])
        cities = data_dict[country]
        for city in cities:
            city_data = cities[city]
            city_obj = City(city,city_data[0],city_data[1],country,city_data[2],city_data[3])
            country_obj._add_city(city_obj)


if __name__ == "__main__":
    create_cities_countries_from_CSV("worldcities_truncated.csv")
    test_example_countries_and_cities()


            # print(i["country"])
        
  
