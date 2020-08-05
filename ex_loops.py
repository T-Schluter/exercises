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

# sum = 0

# number = input("Please enter a number:")
# while number != "":
#     sum = sum + int(number)
#     number = input("Please enter a number:")
# print(sum)

#Q2 use a for loop to format and print the following list

# mailing_list = [
# ["Roary", "roary@moth.catchers"],
# ["Remus", "remus@kapers.dog"],
# ["Prince Thomas of Whitepaw", "hrh.tomas@royalty.wp"],
# ["Biscuit", "biscit @  whippies.park"],
# ["Rory", "rory @ wippies.park"],
# ]

# for item in mailing_list:
#     print(f"{item[0]} : {item[1]}")


#Q3 use a while loop to ask the user for three names and append them to a list then use a for loop to print the list.

# ask user for 3 names input
#append to a list
# end the loop and print the list

# names = []

# count = 3
# while count > 0:
#     name = input(f"Please enter a name:")
#     names.append(name)
#     count = count -1
# print(names)


#Q4 - Loops

# create the list
# ask the user how many units of each item did they buy
# need a loop to go through the different items on the list
# each item will return a different unit value as inputted by the user
# the units will need to be muliplied by the price value in the list
# once the user stops entering intergers the loop should close and print output. * empty string
# the price needs to add together and print the sum at the bottom of the receipt
# output the receipt Izzys food emporium


groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08] 
]

total_price = 0

for item in groceries:
    unit = int(input(f"How many {item[0]} did you buy?"))
    price = item[1] * unit
    print(f"{unit:<5} {item[0]:<20} ${price:.2f}")
    total_price = price + total_price 
    
print()
print("===== Izzy's Food Emporium =====")

for item in groceries:
    print(f"{unit:<5} {item[0]:<20} ${price:.2f}")

print("================================")

print(f"                        ${total_price:.2f}")

#print({item[1]} * unit)

# while count > 0:
#     while number != "":
    # price = {item[1]} * unit
    # count = count -1

# for item in groceries
    #print(f"{item[0]:<20} ${item[1]:.2f}")

print()
    