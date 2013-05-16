def hotel_cost(nights):
	return (140 * nights)
    
def plane_ride_cost(city):
    if (city == "Charlotte"):
        return 183
    elif (city == "Tampa"):
        return 220
    elif (city == "Pittsburgh"):
        return 222
    elif (city == "Los Angeles"):
        return 475
  
def rental_car_cost(days):
	cost = 40 * days
	if (days >= 7):
		cost -= 50
	elif (days >= 3):
		cost -= 20
	return cost

def trip_cost(city, days):
    total = 0
    total += rental_car_cost(days)
    total += hotel_cost(days)
    total += plane_ride_cost(city)
    return total

if __name__ == "__main__":
	print "Hello World" 
	print trip_cost("Los Angeles", 0)