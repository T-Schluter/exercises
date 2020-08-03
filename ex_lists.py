# List exercises

#Q1

foods = ["orange", "apple", "banana", "strawberry", "grape", "blueberry", ["carrot", "cauliflower", "pumpkin"], "Passionfruit", "mango", "kiwifruit"]

print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[0:3])
print(foods[-1:-3])
print(foods[-1][-1])

print()

#Q2

mailing_list = [
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.tomas@royalty.wp"],
["Biscuit", "biscit @  whippies.park"],
["Rory", "rory @ wippies.park"],
]

for item in mailing_list:
    print(f"{item[0]} : {item[1]}")

print ()

#Q3 

# step one ask the user for 3 names
#create counter for 3
# while the counter is greater then zero
# ask the user for their name
# 2 append the names to a list
# 3 print the list

names = []

#empty list

count = 3
while count > 0:
    name = input(f"What is your name?")
    names.append(name)
    count = count -1
print(names)


print()


#Q4 still in development 

text = "this is a string"

# print(len)
# print (text[:14])

string = input()

print ("this is a string")



print()

print("what a lovely day!")