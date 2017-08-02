from sys import argv
# read the WYSS section for how to run this
script, gg, dd= argv
tt = input("tell me your name: ")

print("The script is called:", script)
print("Your first variable is:", gg)
print("Your second variable is:", dd)
print("Your third variable is:", tt)


# Study Drills

# Try giving fewer than three arguments to your script. See that error you get? See if you can explain it.
print("Error: not enough values to unpack( expected 4, got 3)")

# Write a script that has fewer arguments and one that has more. Make sure you give the unpacked variables good names.
print("Done")
# Combine input with argv to make a script that gets more input from a user. Don't overthink it. Just use argv to get something, and input to get something else from the user.
print("Done")
# Remember that modules give you features. Modules. Modules. Remember this because we'll need it later.
