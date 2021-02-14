
# # Print Arguments
# print("The answer is", 42, "always", sep=': ', end='')
# print("(I think)")

# # String Methods
# str = "Hello       .         "
# print(str.rstrip())

# String Formatting
# planets = {'mercury': 57.91,
# 'menus': 108.2,
# 'earth': 149.597870,
# 'mars': 227.94
# }
#
# for i, key in enumerate(planets.keys(), 1):
#     print("{:2f} {:<10s} {:06.2f} Gm".format(i, key.capitalize(), planets[key]))

# Literal string interpolation

# names = ['Tom', 'Harry', 'Jane', 'Mary']
# s = f"The third member is {names[3]}"
# print(s)
# for i, key in enumerate(planets.keys(), 1):
#     print(f"{i:2d} {key.lower():<10s} {planets[key] :06.2f} Gm")


# literal string interpolation 2

# suffix = ['1st', 'nd', 'rd', 'th']
# n = 2
# s = f"{str(n+1) + suffix[n]} of {len(names) : >8d} : {names[n]: >10s} "
# print(s)

# STRING METHODS -SPLIT AND JOIN

line = 'root::0:0:superuser:/root:bin/sh'
elems = line.split(':')
print(elems)
elems[0] = 'avatar'
elems[4] = 'The super-user (zero)'
print(elems)

line = ':'.join(elems)
print(line)
