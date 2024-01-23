# Number of People in the Bus

# There is a bus moving in the city which takes and drops some people at each bus stop.

# You are provided with a list (or array) of integer pairs. Elements of each pair represent the number of people that get on the bus (the first item) and the number of people that get off the bus (the second item) at a bus stop.

# Your task is to return the number of people who are still on the bus after the last bus stop (after the last array). Even though it is the last bus stop, the bus might not be empty and some people might still be inside the bus, they are probably sleeping there :D

# Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the returned integer can't be negative.

# The second value in the first pair in the array is 0, since the bus is empty in the first bus stop.

# Examples:
# [[10,0],[3,5],[5,8]] => 5
# [[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]] => 17
# [[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]] => 21



def count_people_bus(bus_stop):
     # people to 0
    total_people = 0
    for on, off in bus_stop:
        total_people += on - off
    # for on, get off in the bus stops
    return(total_people)
bus_stop = [[10,0],[3,5],[5,8]]
bus_stop = [[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]
bus_stop = [[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]
print(count_people_bus(bus_stop))