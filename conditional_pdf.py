
# # Chained comparison
# number = int(input("enter a number: "))
# distance = int(input("enter a distance: "))
#
# if 0 < number < 42 < distance:
#     print("number and distance are within range")
# else:
#     print("number and distance are out of range")
#
# if 0 < number and number < 42 and 42 < distance:
#     print("number and distance are within range")
# else:
#     print("number and distance are out of range")
#
# if 0 < number < 42 and distance != 20:
#     print ("number is within range and distance is not equal to 20")

# # Sequence and collection tests
# mylist = [0, 1, 2, 3]
# if mylist:
#     print("mylist is True")
#
# print(all(mylist)) # all checks if each item in turn is True or False
#
# if not all(mylist):
#     print("mylist: not all are True")
#
# if any(mylist):
#     print("mylist: at least one item is True")

# # While loops
# line = None
#
# while line != 'done':
#     line = input('Type "done" to complete: ')
#     print('<', line, '>')

# myl = [23, 67, 32, 9, 77]
#
# while myl:
#     print(myl.pop() *2)

# # Loop control statements
# i = 1
# j = 120
#
# while i < 42:
#     i = i * 2
#     if i > j: break
# else:
#     print("Loop expired: ", i)
#
# print("Final value: ", i)

# # For loops
# import sys
#
# for arg in sys.argv:
#     print("Cmd line argument: ", arg)

# # Enumerate
# for idx, arg in enumerate(sys.argv):
#     print('index:', idx, 'argument:', arg)

# for nr, line in enumerate(open('song.txt'), start=1):
#     if nr < 5:
#         print(nr, line, end="")

# # Shorthand conditionals
# i = 42
# j = 3
#
# print("i gt j") if i > j else print ("i lt j")
#
# print("i gt j" if i > j else "i lt j")
#
# a = -1 if i < j else (+1 if i > j else 0)
# print(a)

a = 54
answer = a + (5 if a < 42 else 0)
# answer = a + 5 (if a < 42 else 0) # syntax error
print(a)

# Unconditional closedown
import os
import sys

# os._exit(123) # changes the integer of the exit code
# os.abort()
sys.exit("This is the end.")

print("This will never be printed.")