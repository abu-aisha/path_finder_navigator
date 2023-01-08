import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import math

from vehicles import create_example_vehicles
import city_country_csv_reader
from locations import Country, City
from vehicles import Vehicle, CrappyCrepeCar, DiplomacyDonutDinghy, TeleportingTarteTrolley
from path_finding import find_shortest_path
from map_plotting import plot_trip
import time
from tqdm import tqdm
from trip import Trip, create_example_trips

from city_country_csv_reader import create_cities_countries_from_CSV


##############<----------VEHICLES FUNCTIONS---------------------------->

vehicles = []
make_fleet_opts = None
drpd_car_opts = None

def vehicle_func(event):
    '''
    Event called to choose a format of making a fleet of cars
    '''
# 'From example fleet':
    global drpd_car_opts,make_fleet_opts,vehicles
    
    make_fleet_opts = drpd.get()
    # [,]
    if make_fleet_opts == 'From example fleet':
        # Removing the widgets already formed from other options
        for i in range(2,5):
            for j in range(1,3):
                if frame0.grid_slaves(i,j):
                    frame0.grid_slaves(i,j)[0].grid_remove()
        vehicles =create_example_vehicles()
        h = " , ".join([str(i) for i in vehicles])
        print(h)
        mn.set(f"Your fleet::: {h}")
        # toen.config(state="normal")
        # toen.insert(0,h)
        # toen.config(state="disabled")

    elif make_fleet_opts == "Create manually":
    
        intvar0 = tk.IntVar()
        drpd_cars =tk.Label(frame0,text = "Choose type of car:",font=("Arial Bold",8)  ,  bg = 'grey')
        drpd_car_opts = ttk.Combobox(frame0, textvariable=intvar0)# postcommand= env_try)
        drpd_car_opts["values"] = ['CrappyCrepeCar',"DiplomacyDonutDinghy","TeleportingTarteTrolley"]#("1","2","3","4","5")
        drpd_car_opts.bind('<<ComboboxSelected>>', cars_vals)


        drpd_cars.grid(row=2, column=1)
        drpd_car_opts.grid(row=2,column=2)

        # drpd_cars.place(x = 15, y=50)
        # drpd_car_opts.place(x = 300 , y=50)

def cars_vals(event):
    '''
    Event called to choose a car type in manual selection of cars fleet.
    '''

    global ccc_val_ety,ddd_val_ety1,ddd_val_ety2,ttt_val_ety1,ttt_val_ety2
   
    ddopt_val = drpd_car_opts.get() 


    # frame2 = tk.Frame(frame1 , bg ='grey')
    # frame2.grid(row=1,column=1)
    # frame2.place(relheight=0.4 , relwidth=0.5 ,relx=.20 ,rely=.50)

    
    if ddopt_val == "CrappyCrepeCar":
        # Removal of widgets from other choices of cars
        for i in range(3,5):
            for j in range(1,3):
                if frame0.grid_slaves(i,j):
                    frame0.grid_slaves(i,j)[0].grid_remove()

        
        # b_lb =tk.Label(frame,text = "b",font=("Arial Bold",8)  ,  bg = 'grey')
        # b_en =  tk.Entry(frame,width= 15)

        ccc_val_lab = tk.Label( frame0,text = "CCC speed:", font=("Arial Bold",8)  ,  bg = 'grey' )
        ccc_val_ety = tk.Entry(frame0,width= 15)

        ccc_val_lab.grid(row=3,column=1)
        ccc_val_ety.grid(row=3,column=2)

        print("\nwidgets len",len(frame0.grid_slaves()),"\n")
        
    
    elif ddopt_val =='DiplomacyDonutDinghy':
        # Removal of widgets from other choices of cars
        for i in range(3,5):
            for j in range(1,3):
                if frame0.grid_slaves(i,j):
                    frame0.grid_slaves(i,j)[0].grid_remove()

       
        #WIDGETS
        ddd_val_lab1 = tk.Label(frame0, text = "DDD in country speed:", font=("Arial Bold",8)  ,  bg = 'grey' )
        ddd_val_ety1 = tk.Entry(frame0,width= 15)

        ddd_val_lab2 = tk.Label(frame0, text = "DDD between country speed:", font=("Arial Bold",8)  ,  bg = 'grey' )
        ddd_val_ety2 = tk.Entry(frame0,width= 15)
        ### GEOMETRY
        ddd_val_lab1.grid(row=3,column=1)
        ddd_val_ety1.grid(row=3,column=2)

        ddd_val_lab2.grid(row=4,column=1)
        ddd_val_ety2.grid(row=4,column=2)

        print("\nwidgets len",len(frame0.grid_slaves()),"\n")

        

    elif ddopt_val =="TeleportingTarteTrolley":
        # Removal of widgets from other choices of cars
        for i in range(3,5):
            for j in range(1,3):
                if frame0.grid_slaves(i,j):
                    frame0.grid_slaves(i,j)[0].grid_remove()
        #WIDGETS
        ttt_val_lab1 = tk.Label(frame0, text = "TTT travel time:", font=("Arial Bold",8)  ,  bg = 'grey' )
        ttt_val_ety1 = tk.Entry(frame0,width= 15)

        ttt_val_lab2 = tk.Label(frame0, text = "TTT maximum distance:", font=("Arial Bold",8)  ,  bg = 'grey' )
        ttt_val_ety2 = tk.Entry(frame0,width= 15)
        ### GEOMETRY
        ttt_val_lab1.grid(row=3,column=1)
        ttt_val_ety1.grid(row=3,column=2)

        ttt_val_lab2.grid(row=4,column=1)
        ttt_val_ety2.grid(row=4,column=2)

        print("\nwidgets len",len(frame0.grid_slaves()),"\n")
def update_vehi_disp():
    '''
    function to display the vehicles added to the fleet (for manual creation of fleet)
    '''
    h = " , ".join([str(i) for i in vehicles])
    print(h)
    mn.set(f"Your fleet::: {h}")
        

def add_vehi():
    '''
    function for adding the vehicles to the vehicles list (for manual creation of fleet)
    '''
    if drpd_car_opts:
        ddopt_val = drpd_car_opts.get() 

        if ddopt_val == "CrappyCrepeCar":
            ccc_speed = ccc_val_ety.get()
            if ccc_speed.isdigit():
                car = CrappyCrepeCar(int(ccc_speed))
                vehicles.append(car)
                print(vehicles)
                update_vehi_disp()
            else:
                messagebox.showerror("Error","Only integer values are allowed")
                print("Error!!! Only integer values are allowed") 
        elif  ddopt_val =='DiplomacyDonutDinghy':
            ddd_inspeed = ddd_val_ety1.get()
            ddd_btwspeed = ddd_val_ety2.get()
            if ddd_inspeed.isdigit() and ddd_btwspeed.isdigit():
                car = DiplomacyDonutDinghy(int(ddd_inspeed),int(ddd_btwspeed))
                vehicles.append(car)
                print(vehicles)
                update_vehi_disp()
            else:
                messagebox.showerror("Error","Only integer values are allowed")
                print("Error!!! Only integer values are allowed") 
        elif ddopt_val =="TeleportingTarteTrolley":
            t_time = ttt_val_ety1.get()
            max_dist = ttt_val_ety2.get()
            if t_time.isdigit() and max_dist.isdigit():
                car = TeleportingTarteTrolley(int(t_time),int(max_dist))
                vehicles.append(car)
                print(vehicles)
                update_vehi_disp()
            else:
                messagebox.showerror("Error","Only integer values are allowed")
                print("Error!!! Only integer values are allowed") 
    else:
        messagebox.showerror("Error","This button can only be used after using the manual making of fleet option")
        print("Error!!! This button can only be used after using the manual making of fleet option") 

##############<----------TRIP FUNCTIONS---------------------------->

country_city_data = create_cities_countries_from_CSV("worldcities_truncated.csv",8)

compl_dict= country_city_data[0]
countries_list = country_city_data[1]
make_trip_opts = ''

trip = ''
# Example trips
trips =create_example_trips()
#  sp_from_and_to
trip_man_lst =[]

sp_from_and_to = []

def trip_func(event):
    '''
    Event called when user selects how they want to create their trip
    '''

    global ex_trip_opt_combo,make_trip_opts,countries_combo,cities_combo
    # ['From example trip',"Manually adding all cities","Find shortest path"]
    make_trip_opts = drpd1.get()
    # [,]
    if make_trip_opts == 'From example trip':
        for i in range(2,8):
            for j in range(1,3):
                if frame0a.grid_slaves(i,j):
                    frame0a.grid_slaves(i,j)[0].grid_remove()
         # A list of trip therefore has to choose

        intvar1a = tk.IntVar()
        ex_trip_opt_lab = tk.Label(frame0a,text="Select a trip from Example trips:",font=("Arial Bold",8),bg = 'grey')
        ex_trip_opt_combo = ttk.Combobox(frame0a,textvariable= intvar1a)
        ex_trip_opt_combo["values"] = ["melbourne->sydney","canberra->tokyo","melbourne->canberra->tokyo","canberra->melbourne->tokyo"]

        ex_trip_opt_lab.grid(row=2, column=1)
        ex_trip_opt_combo.grid(row=2,column=2)

        ex_trip_opt_combo.bind("<<ComboboxSelected>>",ex_trip_opts)
        
        # toen.config(state="normal")
        # toen.insert(0,h)
        # toen.config(state="disabled")

    elif make_trip_opts == "Manually adding all cities":
        for i in range(2,8):
            for j in range(1,3):
                if frame0a.grid_slaves(i,j):
                    frame0a.grid_slaves(i,j)[0].grid_remove()


        intvar0a = tk.IntVar()
        countries_lab =tk.Label(frame0a,text = "select country:",font=("Arial Bold",8)  ,  bg = 'grey')
        countries_combo = ttk.Combobox(frame0a, textvariable=intvar0a)# postcommand= env_try)
        countries_combo["values"] = sorted(countries_list)   #("1","2","3","4","5")
        
        

        countries_lab.grid(row=2, column=1)
        countries_combo.grid(row=2,column=2)

        cities_lab =tk.Label(frame0a,text = "select city:",font=("Arial Bold",8)  ,  bg = 'grey')
        cities_combo = ttk.Combobox(frame0a,text= "Select")# textvariable=intvar0a)# postcommand= env_try)
        cities_combo["values"] = []

        cities_lab.grid(row=3, column=1)
        cities_combo.grid(row=3,column=2)
        countries_combo.bind('<<ComboboxSelected>>', fill_city)
    elif make_trip_opts == "Find shortest path":
        for i in range(2,5):
            for j in range(1,3):
                if frame0a.grid_slaves(i,j):
                    frame0a.grid_slaves(i,j)[0].grid_remove()

        intvar0a = tk.IntVar()
        countries_lab =tk.Label(frame0a,text = "select country:",font=("Arial Bold",8)  ,  bg = 'grey')
        countries_combo = ttk.Combobox(frame0a, textvariable=intvar0a)# postcommand= env_try)
        countries_combo["values"] = sorted(countries_list)   #("1","2","3","4","5")
        
        

        countries_lab.grid(row=2, column=1)
        countries_combo.grid(row=2,column=2)

        cities_lab =tk.Label(frame0a,text = "select city:",font=("Arial Bold",8)  ,  bg = 'grey')
        cities_combo = ttk.Combobox(frame0a,text= "Select")# textvariable=intvar0a)# postcommand= env_try)
        cities_combo["values"] = []

        cities_lab.grid(row=3, column=1)
        cities_combo.grid(row=3,column=2)
        countries_combo.bind('<<ComboboxSelected>>', fill_city)


def ex_trip_opts(event):
    global trip
    '''
    Event called to get the trip user has chosen from example trip
    '''

    sel_trip = ex_trip_opt_combo.get()
    if sel_trip == "melbourne->sydney":
        trip = trips[0]
    elif sel_trip == "canberra->tokyo":
        trip = trips[1]
    elif sel_trip == "melbourne->canberra->tokyo":
        trip = trips[2]
    elif sel_trip == "canberra->melbourne->tokyo":
        trip = trips[3]

    mn1.set(f"Your trip::: {trip}")


def fill_city(event):
    global cities_combo,city_id_dict
    country = countries_combo.get()
    cities_fldata = compl_dict[country]
    cities  = list(cities_fldata.keys())
    cities_combo["values"] = cities
    city_id_dict = {}
    for city,data_lst  in cities_fldata.items():
        city_id_dict[city] = data_lst[-1]
    # cities_combo.bind('<<ComboboxSelected>>', add_trip)


def update_trip_disp(*m):
    if m:
        h = " , ".join([str(i) for i in sp_from_and_to])
        if len(sp_from_and_to) ==1:
            # mn1.set("")
            mn1.set(f"Your first city for shortest path ::: {h}")
        elif len(sp_from_and_to) ==2:
            # mn1.set("")
            mn1.set(f"Your two cities for shortest path ::: {h}")

    else:
        mn1.set(f"Your trip::: {str(trip)}")
    



def add_trip():
    global trip,sp_vehi_combo,man_vehi_dict,ex_vehi_dict
    
    if make_trip_opts:
        if make_trip_opts =="Manually adding all cities":
            city_ascii = cities_combo.get() 
            city_id = city_id_dict[city_ascii]
            city_obj = City.cities[city_id]
            if not trip_man_lst:
                trip = Trip(city_obj)
            else:
                trip.add_next_city(city_obj)
            trip_man_lst.append(city_obj)
            update_trip_disp()
            print(city_obj)

        elif make_trip_opts == "Find shortest path":
            city_ascii = cities_combo.get() 
            city_id = city_id_dict[city_ascii]
            city_obj = City.cities[city_id]
            
            if len(sp_from_and_to) <2:
                sp_from_and_to.append(city_obj)
                update_trip_disp(9)
                
            else:
                messagebox.showerror("Error","You can not add more than two cities")
                print("You can not add more than two cities") 

            if len(sp_from_and_to) ==2:
                # You need to check if vehicles have been selected too
                    if make_fleet_opts:
                        sp_vehi_int = tk.IntVar()
                        sp_vehi_lb =tk.Label(frame0a,text = "Select vehicle for shortest path from your fleet:",font=("Arial Bold",8)  ,  bg = 'grey')
                        sp_vehi_combo = ttk.Combobox(frame0a, textvariable=sp_vehi_int)# postcommand= env_try)
                        if make_fleet_opts == "From example fleet":
                            ex_vehi_dict = {}
                            for vehicle_obj in vehicles:
                                ex_vehi_dict[str(vehicle_obj)] = vehicle_obj
                            sp_vehi_combo["values"] = list(ex_vehi_dict.keys())
                        elif make_fleet_opts == 'Create manually':
                            man_vehi_dict = {}
                            for vehicle_obj in vehicles:
                                man_vehi_dict[str(vehicle_obj)] = vehicle_obj
                            sp_vehi_combo["values"] = list(man_vehi_dict.keys())

                        sp_vehi_lb.grid(row=6,column=1)
                        sp_vehi_combo.grid(row=6,column=2)

                        reset_sp_cities_btn = tk.Button(frame0a,text = "Reset shortest path cities" ,command=rset_sp_cities)
                        reset_sp_cities_btn.grid(row=7,column=1)

                        sp_trip_btn = tk.Button(frame0a,text = "Get shortest path trip" ,command=calc_sp_trip)
                        sp_trip_btn.grid(row=7,column=2)

                        

                    else:
                        messagebox.showerror("Error","You have made no fleet, please make your fleet of cars")
                        print("You have made no fleet, please make your fleet of cars") 
        
    else:
        messagebox.showerror("Error","This button can only be used after choosing to make a trip manually or by shortest path")
        print("This button can only be used after choosing to make a trip manually or by shortest path") 
        
def rset_sp_cities():
    global sp_from_and_to
    sp_from_and_to = []


def calc_sp_trip():
    global trip
    sp_vehi_str = sp_vehi_combo.get()
    if make_fleet_opts:
        if make_fleet_opts == "From example fleet":
            sp_vehi = ex_vehi_dict[sp_vehi_str]
        elif make_fleet_opts == "Create manually":

            sp_vehi = man_vehi_dict[sp_vehi_str]
        trip = find_shortest_path(sp_vehi,sp_from_and_to[0],sp_from_and_to[1])
        if trip == None:
            messagebox.showinfo("Notice","Your finding of shortest path yield no result, Try other cities")
            print("Your finding of shortest path yield no result, Try other cities") 
        else:
            messagebox.showinfo("Message","Shortest path successfully found")
            print("Shortest path successfully found")
            mn1.set(f"Your trip::: {str(trip)}")

def get_fastest_vehi():
    if vehicles:
        if trip:
            fastest_v,time_v = trip.find_fastest_vehicle(vehicles)
            print(fastest_v,time_v)
        else:
            messagebox.showerror("Error","You have made no trip, try to make one")
            print("You have made no trip, try to make one") 
    else:
        messagebox.showerror("Error","You have made no fleet, please make your fleet of cars")
        print("You have made no fleet, please make your fleet of cars") 

    




my_app = tk.Tk()
my_app.title("manager")


canvas = tk.Canvas(my_app ,height=1000 , width=1000  ,bg='#263D42', bd = 6)
canvas.pack()


frame = tk.Frame(canvas , bg ='grey')
frame.place(relheight=0.95 , relwidth=0.95 ,relx=.025 ,rely=.025)

framea = tk.Frame(frame , bg ='green')
framea.place(relheight=0.20 , relwidth=0.95 ,relx=.025 ,rely=.025)

frameb = tk.Frame(frame , bg ='red')
frameb.place(relheight=0.75 , relwidth=0.95 ,relx=.025 ,rely=.230)



frame0 = tk.Frame(frameb , bg ='blue')
frame0.grid(row = 1,column = 1,ipady=.5, ipadx=.9)

frame0a = tk.Frame(frameb , bg ='blue')
frame0a.grid(row = 1,column = 2, ipady=.5, ipadx=2.0)

#################-------------------<# FLEET >-------------------------------

# fleet text update
mn = tk.StringVar(value = "")
toen = tk.Label(framea , textvariable=mn,font=("Arial Bold",10))

toen.place(x = 50, y=30)

# FLEET BASE
mc = tk.IntVar()
drpd_lb =tk.Label(frame0,text = "HOW DO YOU WANT TO CREATE YOUR FLEET:",font=("Arial Bold",8)  ,  bg = 'grey')
drpd = ttk.Combobox(frame0, textvariable=mc)# postcommand= env_try)

drpd_lb.grid(row=1,column=1)
drpd.grid(row=1,column=2)


drpd["values"] = ['From example fleet',"Create manually"]#("1","2","3","4","5")
drpd.bind('<<ComboboxSelected>>', vehicle_func)

# Add vehicle button widget
add_car = tk.Button(frame0,text="Add vehicle" ,command=add_vehi)
add_car.grid(row=5,column=1,columnspan=2)

#################-------------------<# TRIP >-------------------------------

# trip text update
mn1 = tk.StringVar(value = "")
toen1 = tk.Label(framea , textvariable=mn1,font=("Arial Bold",10))

toen1.place(x = 50, y=50)


# BASE
mc1 = tk.IntVar()
drpd_lb1 =tk.Label(frame0a,text = "HOW DO YOU WANT TO CREATE YOUR TRIP:",font=("Arial Bold",8)  ,  bg = 'grey')
drpd1 = ttk.Combobox(frame0a, textvariable=mc1)# postcommand= env_try)


drpd_lb1.grid(row=1,column=1)
drpd1.grid(row=1,column=2)

drpd1["values"] = ['From example trip',"Manually adding all cities","Find shortest path"]#("1","2","3","4","5")
drpd1.bind('<<ComboboxSelected>>', trip_func)

add_city = tk.Button(frame0a,text="Add city" ,command=add_trip)
add_city.grid(row=8,column=1,columnspan=2)

get_fst_vehibtn = tk.Button(frame0a,text="Get fastest vehicle" ,command=get_fastest_vehi)
get_fst_vehibtn.grid(row=9,column=1,columnspan=2)



my_app.mainloop()

