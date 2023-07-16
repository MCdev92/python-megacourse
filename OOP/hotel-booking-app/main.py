import pandas

df = pandas.read_csv("OOP/hotel-booking-app/hotels.csv")
class Hotel:
    def __init__(self, id):
       pass
    def book(self):
        pass
    
    def avaliabel(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass
    def generate(self):
        pass

print(df)
id = input("Enter the id of the hotel: ")
hotel = Hotel(id)
if hotel.avaliable():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free.")
    

