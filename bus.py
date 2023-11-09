'''
BINDU KABUSARA JOSUE S22B13/011

PROJECT NAME: BUS MANAGEMENT SYSTEM
I CREATED THIS PROJECT BECAUSE MOST OF TIME WHEN I TRAVEL BY BUS USING JAGUAR AGENCY 
I HAVE NOTICED THAT THEY HAVE A BAD MANAGEMENT BECAUSE SOMETIME I PAY BUT I WILL NOT FIND WHERE TO SIT
'''

class Passenger:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Bus:
    def __init__(self, capacity):
        self.capacity = capacity
        self.available_seats = list(range(1, capacity + 1))
        self.passengers = {}

    def book_seat(self, passenger, seat_number):
        if seat_number in self.available_seats:
            self.available_seats.remove(seat_number)
            self.passengers[seat_number] = passenger
            print(f"Seat {seat_number} booked for {passenger.name}")
        else:
            print(f"Seat {seat_number} is already booked or invalid.")

    def display_seats(self):
        print("Available Seats:", self.available_seats)
        print("Booked Seats:", list(self.passengers.keys()))

    def are_all_seats_booked(self):
        return len(self.available_seats) == 0

    def display_passenger_info(self, seat_number):
        passenger = self.passengers.get(seat_number)
        if passenger:
            print(f"Tank you for choosing JAGUAR Bus🚌 \nPassenger Information for Seat:\n {passenger.name} has taken the seat number: {seat_number}:")
            
            print(f"Age: {passenger.age}")
            print(f"Gender: {passenger.gender}")
        else:
            print(f"No passenger found for Seat {seat_number}")

class VIPBus(Bus):
    def __init__(self, capacity):
        super().__init__(capacity)
        self.vip_seats = list(range(1, min(1, capacity + 1)))

    def book_seat(self, passenger, seat_number):
        if seat_number in self.vip_seats:
            self.vip_seats.remove(seat_number)
            print(f"VIP Seat {seat_number} booked for {passenger.name}")
        else:
            super().book_seat(passenger, seat_number)

    def are_all_vip_seats_booked(self):
        return len(self.vip_seats) == 0

# Example usage:
def main():
    #bus=None
    bus_type = input("BOOK A TICKET(🎟) \n JAGUAR BUS 🚌\nChoose bus type (VIP/Regular): ").lower()

    if bus_type == 'vip':
        bus = VIPBus(10)
    elif bus_type == 'regular':
        bus = Bus(30)
    else:
        print("we dont have that bus type at JAGUAR BUS") 

    while not bus.are_all_seats_booked():
        bus.display_seats()

        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        gender = input("Enter your gender: ")

        passenger = Passenger(name, age, gender)

        seat_number = int(input("Choose a seat number: "))
        bus.book_seat(passenger, seat_number)

        bus.display_passenger_info(seat_number)

    if isinstance(bus, VIPBus) and bus.are_all_vip_seats_booked():
        print("VIP Seats are no longer available.❌")
    else:
        print("Regular Seats are no longer available.❌")

if __name__ == "__main__":
    main()

