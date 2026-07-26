class Car:
    def __init__(self, make, model, year):
        self._make = make  # Private attribute
        self._model = model  # Private attribute
        self._year = year  # Private attribute

    # Public method to get car details
    def get_details(self):
        return f"{self._year} {self._make} {self._model}"

    # Public method to set car details
    def set_details(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
class moto:
    def __init__(self, make, model, year):
        self._make = make  # Private attribute
        self._model = model  # Private attribute
        self._year = year  # Private attribute

    # Public method to get car details
    def get_details(self):
        return f"{self._year} {self._make} {self._model}"

    # Public method to set car details
    def set_details(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year


# Create an instance of the Car class
my_car = moto("Toyota", "Corolla", 2020)

# Accessing public method to get car details
print(my_car.get_details())  # Output: 2020 Toyota Corolla

# Modifying car details using public method
my_car.set_details("Honda", "Civic", 2022)

# Accessing public method to get updated car details
print(my_car.get_details())  # Output: 2022 Honda Civic

# Trying to access private attributes directly (will raise an AttributeError)
print(my_car._make)  # This will raise an AttributeError
