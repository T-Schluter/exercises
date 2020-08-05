# Functions Exercises

#Q1

def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius

    Args:
        temp_in_farenheit: integer representing a temperature.
    Returns:
        An integer representing a temperature in degrees celcius.
    """
    #T(°C) = (T(°F) - 32) × 5/9

    temp_celcius = (temp_in_farenheit - 32) * 5 / 9
    print(temp_celcius)
    return int(temp_celcius)

convert_f_to_c(97)
convert_f_to_c(32)

#Q2 

# create a empty list
# program to ask user for number input
# store numbers in list
# once user enters blank stop asking for user input
# sum of the intergers in the list
# keep a count of the user inputs
# calculate the mean of the input intergers


def calculate_mean():

    numbers = []
    count = 0
    sum = 0

    user_input = input("Please enter a number: ")
    numbers.append(user_input)
    while user_input != "":
        user_input = input("Please enter a number: ")
        if user_input == "":
            break
        numbers.append(user_input)
        count += 1
    print(numbers)
    for num in numbers:
        sum = int(num) + sum

    print(sum)
    print(sum / count)
    return sum / count

average = calculate_mean()


    

