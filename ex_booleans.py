# Booleans and If Statement Exercises

#Q1

moths_in_house = False
if moths_in_house:
    print("Roary go get the moths!")
else:
    print("No threats detected.")


print()

#Q2

moths_in_house = False
mitch_is_home = True

if moths_in_house and mitch_is_home:
    print("Hooman! Help me get the moths")

elif not moths_in_house and not mitch_is_home:
    print("No treats detected.")


elif moths_in_house and not mitch_is_home:
    print("Meoooooooow! Hisssssssss")

elif not moths_in_house and not mitch_is_home:
    print("Climb on Mitch.")

print()

#Q3

is_car_detected = False
is_red = True

if is_car_detected and is_red:
    print("FLash!")

else:
    print("do nothing.")
print()

#Q4

height_limit = 120

height_check = int(input("Please enter your height in centimeters: "))

if height_check < height_limit:
    print("Sorry, not today.")

else:
    print("Yay, Hop on!")


# Completed.