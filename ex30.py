people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")


# Study Drills

# Try to guess what elif and else are doing.
print("elif: another condition, else: others conditions.")
# Change the numbers of cars, people, and trucks, and then trace through each if-statement to see what will be printed.
# Try some more complex boolean expressions like cars > people or trucks < cars.
# Above each line write an English description of what the line does.
