#  Hint:  You may not need all of these.  Remove the unused functions.

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination



def reconstruct_trip(tickets, length):
    hash_table = {}
    trip_array = [None] * length #
    """
    YOUR CODE HERE
    """
    # Your code here
    for object in range(length):
        if tickets[object].source == "NONE":
            trip_array[0] = tickets[object].destination
        #print("tickets[object]: ",tickets[object].source)
        #print(trip_array)
        #print("source: ", object.source, "destination: ", object.destination)
        hash_table[tickets[object].source] = tickets[object].destination 
    #return route
    for i in range(length):
        print("i: ",i)
        if trip_array[i] in hash_table:
            print('---->',trip_array[i])
            trip_array[i] =  hash_table[trip_array[i]]
    return trip_array


tickets = [
    Ticket("PIT","ORD"),
    Ticket("XNA","CID"),#3
    Ticket("SFO","BHM"),
    Ticket("FLG","XNA"),
    Ticket("NONE","LAX"),#beginning
    Ticket("LAX","SFO"),#1
    Ticket("CID","SLC"),
    Ticket("ORD","NONE"),#5
    Ticket("SLC","PIT"),#4
    Ticket("BHM","FLG")#2
]
#     T(1)----------T(2)--------->T(3)---------->T(4)------>T(5)
#["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"] #trip for tickets above
reconstruct_trip(tickets, len(tickets))










