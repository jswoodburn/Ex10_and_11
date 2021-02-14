import getpass

correct_pin = "5742"
entry = ""
tries = 0

while entry != correct_pin and tries < 3:
    entry = str(getpass.getpass("Enter a " + str(len(correct_pin)) + " digit PIN: "))
    if entry.isdecimal() == 0:
        print("Your entry can only be numbers\n")
    elif len(entry) != 4:
        print("Your PIN must be " + str(len(correct_pin)) + " digits\n")
    else:
        if entry == correct_pin:
            print("Your pin is correct.")
            break
        else:
            tries += 1
        print("You have had " + str(tries) + " attempt(s).\n")