# Loops Exercises

#Q1

# set up sum of entered numbers set to 0
# ask user to input intergers 
# while
    # if the user enters an empty string
        # do nothing
    # else 
        # add the number to the total

# != is not equal too

sum = 0

number = input("Please enter a number:")
while number != "":
    sum = sum + int(number)
    number = input("Please enter a number:")
print(sum)

#Q2 use a for loop to format and print the following list

# .

mailing_list = [
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.tomas@royalty.wp"],
["Biscuit", "biscit @  whippies.park"],
["Rory", "rory @ wippies.park"],
]

for item in mailing_list:
    print(f"{item[0]} : {item[1]}")


#Q3 use a while loop to ask the user for three names and append them to a list then use a for loop to print the list.

# ask user for 3 names input
#append to a list
# end the loop and print the list

names = []

count = 3
while count > 0:
    name = input(f"Please enter a name:")
    names.append(name)
    count = count -1
print(names)


#Q4

# 

groceries = [
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08 
]