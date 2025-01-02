class Flight():


    def __init__(self, capacity):
        self.capacity = capacity
        self.len_passengers = 0
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) >= self.capacity:
            print("The flight is full")
            return
        
        self.passengers.append(passenger)
        self.len_passengers += 1

my_flight = Flight(capacity=3)
my_flight.add_passenger("Daniel")
my_flight.add_passenger("Luis")
my_flight.add_passenger("Martin")
my_flight.add_passenger("Juan")