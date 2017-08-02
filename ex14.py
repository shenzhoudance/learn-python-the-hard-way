from sys import argv

script, user_name, age = argv
x = '>'

print(f"Hi {user_name}, I'm the {script} script. I am {age} years old.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}")
likes = input(x)

print(f"Where do you live {user_name}?")
lives = input(x)

print("What kind of computer do you have?")
computer = input(x)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")


# Study Drills

# 1.Find out what the games Zork and Adventure were. Try to find a copy and play it.
print("1Done")
# 2.Change the prompt variable to something else entirely.
print("2 Change into the \"x\"")
# 3.Add another argument and use it in your script, the same way you did in the previous exercise with first, second = ARGV.
print("3Done")
# 4.Make sure you understand how I combined a """ style multiline string with the {} format activator as the last print.
print("4Yes")
