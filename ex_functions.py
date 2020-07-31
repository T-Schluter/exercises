# def  create_message(first_name, last_name):
#     # a = 1
#     print(f"Hi {first_name} {last_name}!") 

# create_message("Hayley" "Van Waas")

#google defult functions in python, for future

# create_message("Teagan")
# create_message("Sherie")
# create_message("Boots")

# person = "Teagan"
# create_message(person)


# name = "Felix"
# print(name)
# print(a)

# counter = 5

#while counter > 0:
#    if counter%2 == 0:
#    print(f"{counter} is an even number.")
#    else:
#       print(f"{counter} is an odd number.")
#    counter -= 1


def is_even(number): 
    if number%2 ==0:
        return True
    else:
        return False

#return used instead of print to output, send info back.  save as a variable.
#while loop counter

counter = 5
while counter > 0:
    if is_even(counter):
        print(f"{counter} is an even number.")
    else:
        print(f"{counter} is an odd number.")
    counter -= 1

# counter -=1 will stop the loop.  to cancel loop ctl c
# functions allow things to be seperated out in the logic
# functions are usefull for debug, only change function in one spot.
# bits of code that only run when we need them to run.  Dynamic input


# num2 = is_even(2) send and return info
# num3 = is_even(3)

# print(num2, num3)

def awesome_message(name):
    return f"{name} is awesome"

def generic_greeting(name):
    return f"Hi, {name}"

name = input("What is your name? ")
if name == "Teagan":
    print(awesome_message(name))
else:
    print(generic_greeting(name))

