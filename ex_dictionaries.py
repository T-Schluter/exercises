# dictionaries are a way to structure data , keys and values. 
# Use curly braces to tell python its a dictonary


groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Bacon": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08 
}

print(groceries)


# Change value of existing key:
groceries["Hot Chocolate"] = 11.10,
groceries["Crackers"] = 4.20,
groceries["Carrots"] = 2.24,
groceries["Oranges"] = 6.16,
print(groceries)

# Look up items value in the string
# for item in groceries:
#     print(item, groceries[item])


# # Unpacking Tupple: first item becomes the key second item becomes the tupple. FYI 
# for index, item in enumerate(some_list):


# # Shortcut to printing the key and its value in for loop
# for key, value in groceries.items():
#     print(key, value)

# print(groceries.items())

# print list value within defined keys
cohorts = {
    "perth": ["Anna", "Viv", "Nic", "Teagen"],
    "brisbane": ["Teagan", "Vivian", "Nic", "Joy"]
}

# print(cohorts["perth"])

for cohort, peeps in cohorts.items():
    print(cohort, peeps) #or print(f"{cohort} {peeps}")
    for peep in peeps:
        print(f"      {peep}")

print()

#nest dictonarys in dictonary with loops
all_cohorts = {
    2019: {
        "perth": ["Anna", "Sarah", "Nina", "Ellie"]
    },
    2020: {
        "perth": ["Anna", "Viv", "Nic", "Teagen"],
        "brisbane": ["Teagan", "Vivian", "Nic", "Joy"]
    }
}

#string formating with upper and lower case
for year, cohorts in all_cohorts.items():
    print(year)
    for city, cohort in cohorts.items():
        print(f"     {city.upper()}")
        for peep in cohort:
            print(f"      {peep.lower()}")
