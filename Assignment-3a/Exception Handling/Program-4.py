# Custom Exceptions
class InvalidAgeError(Exception):
    pass

class SeatLimitError(Exception):
    pass


class FlightBooking:
    def __init__(self, name, age, seats):
        self.name = name
        self.age = age
        self.seats = seats

    def book_ticket(self):
        try:
            # Validate age
            if not isinstance(self.age, int) or not isinstance(self.seats, int):
                raise ValueError("Age and seats must be integers.")

            if self.age < 0 or self.age > 120:
                raise InvalidAgeError("Invalid age. Must be between 0 and 120.")

            if self.seats > 6:
                raise SeatLimitError("Cannot book more than 6 seats.")

            # Successful booking
            print(f"Booking successful for {self.name}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except InvalidAgeError as iae:
            print(f"Error: {iae}")
        except SeatLimitError as sle:
            print(f"Error: {sle}")
        except Exception as e:
            print(f"Unexpected Error: {e}")


# ----------- Test Cases -----------

name = input("Enter your name: ")
age = int(input("Enter your age: "))
seats = int(input("Enter your seats: "))
fb = FlightBooking(name, age, seats)
fb.book_ticket()