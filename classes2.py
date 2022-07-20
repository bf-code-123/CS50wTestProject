class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        #start w empty list of passengers
        self.passengers = []

    def add_passenger(self, name):
        #check open seats
        if not self.open_seats():
            return False
        #add passenger to flight
        self.passengers.append(name)
        return True
    
    #new function to get open seats
    def open_seats(self):
        return self.capacity - len(self.passengers)

#creating a flight with capacity of 3
flight = Flight(3)

#create new list
people = ("harry", "ron", "hermione", "ginny")

#iterate through people list
for person in people:
    #save each addition to a variable
    success = flight.add_passenger(person)
    #if sucess was true, message added
    if success:
        print(f"{person} was successfully added")
    #if success was false, message failed
    else:
        print(f"{person} was not added")
