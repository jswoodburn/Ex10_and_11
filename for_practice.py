# friends = ["Jim","Karen","Kevin"]

# for person in friends: # can be for elements in arrays/lists, or indexes in string
#         print(person)
#
# cheese= " Cheese string"
# # for character in cheese:
# #     print(character)
# print(cheese)
# new_cheese = ""
# for i, character in enumerate(cheese):
#     # print(i,character)
#     if i%2 == 0: # if the index is even
#         # print("even!")
#         new_cheese+=character.upper()
#     else:
#         # print("odd")
#         new_cheese+=character
#     print(new_cheese)
# print(new_cheese)

# # print every number in range from zero, but not 10
# for index in range(10):
#     print(index)
#
# # print every number from 5-15, including 5 but not 15
# for index in range(5, 15):
#     print(index)
# #
# # does the same as the first for loop, but uses range function
# for index in range(len(friends)):
#     print(friends[index])
#
# complex logic inside for loop
for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("not first iteration")