# total of cars
cars = 100
# the positions of every car
space_in_a_car = 4.0
# how many drivers
drivers = 30
# how many passengers
passengers = 90
# the number of cars that is undriven
cars_not_driven = cars - drivers
# the number of cars that is driven
cars_driven = drivers
# the capacity of driven cars
carpool_capacity = cars_driven * space_in_a_car
# average passengers per car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")


print("Study Drills")

# When I wrote this program the first time I had a mistake, and Python told me about it like this:

# Traceback (most recent call last):
#  File "ex4.py", line 8, in <module>
#    average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined
# Explain this error in your own words. Make sure you use line numbers and explain why.

print ("没定义变量 car_pool_capacity, 需要define car_pool_capacity = ? ")

# Here are more study drills:

# I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?

print("I think it unnecessary here. The space_in_a _car is a integer number.")

# Remember that 4.0 is a floating point number. It's just a number with a decimal point, and you need 4.0 instead of just 4 so that it is floating point.

# Write comments above each of the variable assignments.
print("2Done")

# Make sure you know what = is called (equals) and that its purpose is to give data (numbers, strings, etc.) names (cars_driven, passengers).
print("3Done")
# Remember that _ is an underscore character.
print("4Done")
# Try running python3.6 from the Terminal as a calculator like you did before, and use variable names to do your calculations. Popular variable names are also i, x, and j.
print("5Done")
