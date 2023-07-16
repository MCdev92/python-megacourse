import pandas

df = pandas.read_csv("OOP/hotel-booking-app/hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id):
       self.hotel_id = hotel_id
       
       
    def book(self):
        """Book a hotel by changing its avaliability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)
        
    
    def avaliable(self):
        """Check if the hotel is avaliable"""
        avaliability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if  avaliability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass
    def generate(self):
        pass

print(df)
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.avaliable():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free.")
    

