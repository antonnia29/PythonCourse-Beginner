# Antonnia Abdul - AN24020013912

#Pseudocode to calculate a user's total holiday cost, which includes the plane cost, hotel cost and car-rental cost.


"""Steps:
1. create a list of travel destinations
2. Capture and store responses from end user
3. create functions and supporting logic
4. use if statement to capture prize variation based on destination
5. display final holiday cost to user in suitable format

"""

#selection list
flight_list = ["paris","new york", "dubai","barcelona"]
flight_list.sort()


#user data input

try:

     
        print("what city are you travelling to?")
        for x in flight_list:
            print(x.capitalize())

        city_flight = input("\nEnter a city from the options above: ").lower()
        if city_flight not in ["paris","new york", "dubai","barcelona"]:
            raise ValueError("Please enter a city from the choices provided!")
            

        num_nights = int(input("Enter number of nights: "))

        rental_days = int(input("Enter number of car rental days you are hiring: "))

    
except ValueError as e:
    print(f"Error: {e}")
except TypeError as e:
    print(f"Error: {e}")
except NameError as e:
    print(f"Error: {e}")


#charge per night (hotel)
def hotel_cost(num_nights): 
    total_hotel_cost  = num_nights * 130
    return total_hotel_cost


#charge per flight
def plane_cost(city_flight):

    if city_flight == "paris":
        return 300.50
   
    elif city_flight == "new york":
        return 1479
    
    elif city_flight == "dubai":
     return 1189
   
    elif city_flight == ("barcelona"):
        return 769.80
   
    else:
        print("invalid city")



#charge per rental (car)
def car_rental(rental_days):
    total_cost_of_car_rental = rental_days * 45
    return total_cost_of_car_rental


#total holiday cost
def holiday_cost(num_nights, city_flight, rental_days):
    hotel = hotel_cost(num_nights)
    flight = plane_cost (city_flight)
    car = car_rental(rental_days)
    total_cost_of_holiday = int(hotel + flight + car)
    return total_cost_of_holiday


#display summary to user
print("\n-------------------------------------------------------------------------------------------")

message1 = "Below is a COST breakdown of your holiday package, please check our other travel destinations on offer!"


print(f"Holiday Summary\nYou selected a trip to {city_flight}, spending {num_nights} nights, renting a car for {rental_days} days ")

print(f"{message1} \n\n>>Your total hotel cost is: £{hotel_cost(num_nights)}")

print(f">>Your total flight cost is: £{plane_cost(city_flight)}") 

print(f">>Your total rental cost is: £{car_rental(rental_days)}")

print(f"\n>>Total holiday package is: £{holiday_cost(num_nights,city_flight,rental_days)}")





