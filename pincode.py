import getpass

correct_pin = "5742"
entry = ""
tries = 0

while entry != correct_pin and tries < 3:
    entry = str(getpass.getpass("Enter your PIN: "))
    if entry == correct_pin:
        print("Your pin is correct.")
        break
    else:
        tries += 1
    print("You have had " + str(tries) + " attempt(s).")

# while entry != correct_pin:
#     entry = str(input("Enter your PIN: "))
#     if entry == correct_pin:
#         print("Your pin is correct.")
#         break
#     else:
#         tries += 1
#         if tries == 3:
#             break
#     print("You have had " + str(tries) + " attempt(s).")

# print("end of script")
