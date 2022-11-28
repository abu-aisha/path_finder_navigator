
from vehicles import create_example_vehicles
import city_country_csv_reader
from locations import Country, City
from vehicles import Vehicle, CrappyCrepeCar, DiplomacyDonutDinghy, TeleportingTarteTrolley
from path_finding import find_shortest_path
from map_plotting import plot_trip
import time
from tqdm import tqdm


from trip import Trip, create_example_trips





city_country_csv_reader.create_cities_countries_from_CSV("worldcities_truncated.csv")



car_qus ='''
1 for CrappyCrepeCar, Enter in format '1,car_speed'

2 forDiplomacyDonutDinghy,   Enter in format '2, in_country_speed, between_primary_speed'
 
3 for TeleportingTarteTrolley, Enter in format '3, travel_time, max_distance'
Enter 9 to to quit addition of cars:
 '''




while True:

    vehi_input = input('''
    How do you want to create your cars:
    Enter: 
    1 for creating from  example vehicles
    2 for creating your fleet manually
    9 to quit
    Response:  ''')
    halt= ""
    try:
        halt = int(vehi_input)
    except:
        pass

    if halt == 9:
        break
    elif vehi_input.isdigit():
        if int(vehi_input) ==1:
            vehicles =create_example_vehicles()
        elif int(vehi_input) == 2:
            vehicles = []
            while True:

                car_type = input(car_qus)

                halt1 =""
                try:
                    halt1 = int(car_type)
                except:
                    pass
                if halt1 == 9 :
                    break

                elif len(car_type)>0: 
                    if car_type[0].isdigit() and car_type.__contains__(","):
                        lst1 = car_type.split(',')
                        if lst1[0] == '1':
                            if lst1[1].isdigit() and len(lst1) ==2:
                                vehi = CrappyCrepeCar(int(lst1[1]))
                                vehicles.append(vehi)
                            else:
                                print("You have not entered a correct format for CrappyCrepeCar")
                            
                        elif lst1[0] == '2':
                            if lst1[1].isdigit() and lst1[-1].isdigit() and len(lst1) ==3:
                                vehi = DiplomacyDonutDinghy(int(lst1[1]),int(lst1[2]))
                                vehicles.append(vehi)
                            else:
                                print("You have not entered a correct format for DiplomacyDonutDinghy")
                        elif lst1[0] == '3':
                            if lst1[1].isdigit() and lst1[-1].isdigit() and len(lst1) ==3:
                                vehi = TeleportingTarteTrolley(int(lst1[1]),int(lst1[2]))
                                vehicles.append(vehi)
                            else:
                                print("You have not entered a correct format for TeleportingTarteTrolley")
                        else:
                            print("You have not entered an available car option")
                else:
                    print("You have not entered a correct car format")

        print(vehicles)

        trip_q1 = '''Create a trip by:
        Enter 1 to create from example trip and also the index of the example you want to use e.g. 1,2
        -->1 to create from example trip and to use the number 2 example trip , we have only 4 example
        -->therefore, the maximum number should be 4 and minimum 1
        Enter 2 to create manually
        Enter 3 to create by shortest path between two cities:
        Enter 9 to quit
        '''
        
        if len(vehicles) >0:
            while True:
                trip_input = input(trip_q1)
                try:
                    halt2 = int(trip_input)
                except:
                    halt2 =''

                if halt2 ==9:
                    break

                elif trip_input == "1":
                    trip_ex_ind = input('''
                    Choose your trip from the example below
                    1. (melbourne, sydney)
                    2. (canberra, tokyo)
                    3. (melbourne, canberra, tokyo)
                    4. (canberra, melbourne, tokyo)
                    Choose by enter the trip number for example 2 for trip (canberra, tokyo)
                    Your Response:
                    ''')
                    if trip_ex_ind.isdigit():
                        trip = create_example_trips()[int(trip_ex_ind)]
                    else:
                        print("You have not entered a valid option for an example trip")
                elif trip_input == "2":
                    city_input = input("""
                    Enter the city ids for your trip in the format 'cityid_1,cityid_2,....,cityid_n'
                    Your Response:
                    """)
                    if city_input.__contains__(","):
                        city_list = city_input.split(',')
                        for i in range(len(city_list)):
                            if city_list[i].isdigit():
                                pass ###### TO CONTINUE HERE                                                                            

                    x=0
                    for cityid in city_list:    
                        city = City.cities[cityid]
                        if x == 0:
                            trip = Trip(city)
                            x +=1
                        else:
                            trip.add_next_city(city)
                
                elif trip_input == "3":
                    cities = input("Input cities id in format:\n'from_city_id,to_city_id':")
                    cities_lst = cities.split(',')
                    from_city = City.cities[cities_lst[0]]
                    to_city = City.cities[cities_lst[1]]
                    trip = find_shortest_path(vehicles[0], from_city, to_city)

                else:
                    print("You have not entered a valid option on how you want to create your trip")

                fastest_v,time_v = trip.find_fastest_vehicle(vehicles)
                print(fastest_v,time_v)

                if fastest_v != None :
                    plot_trip(trip)

                    for i in tqdm(range(int(time_v))):
                        time.sleep(0.1)
                else:
                    print("Your trip is impossible")
        else:
            print("You have not created any vehicle")

    else:
        print("You have supplied an invalid Input!!!")











# vehicles =create_example_vehicles() 

# custom_vehicles =[CrappyCrepeCar(200), DiplomacyDonutDinghy(100, 500), TeleportingTarteTrolley(3, 2000)]



# trips = []

# for cities in [(canberra, melbourne, tokyo)]:
#     trip = Trip(cities[0])
#     for city in cities[1:]:
#         trip.add_next_city(city)

#         trips.append(trip)