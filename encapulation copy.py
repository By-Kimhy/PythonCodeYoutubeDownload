from encapulation import *
# Create an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing public method to get car details
print(my_car.get_details())  # Output: 2020 Toyota Corolla

# Modifying car details using public method
my_car.set_details("Honda", "Civic", 2022)

# Accessing public method to get updated car details
print(my_car.get_details())  # Output: 2022 Honda Civic

# Trying to access private attributes directly (will raise an AttributeError)
print(my_car._make)  # This will raise an AttributeError
