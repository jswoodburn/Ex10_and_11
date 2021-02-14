
# # Print Arguments
# print("The answer is", 42, "always", sep=': ', end='')
# print("(I think)")

# # String Methods
# str = "Hello       .         "
# print(str.rstrip())

# String Formatting
planets = {'mercury': 57.91,
'menus': 108.2,
'earth': 149.597870,
'mars': 227.94
}

for i, key in enumerate(planets.keys(), 1):
    print("{:2f} {:<10s} {:06.2f} Gm".format(i, key.capitalize(), planets[key]))

# Literal string interpolation

