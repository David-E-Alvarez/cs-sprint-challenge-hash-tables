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
    
    
    return None


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










