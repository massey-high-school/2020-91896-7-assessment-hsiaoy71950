# This component prints the instructions

# This component prints all the choices given to the user and makes them enter a valid option


def multi_choice(question, options):
    numbering = 0

    # Prints all the available options

    for x in options:
        numbering += 1
        print("{}.".format(numbering), x)
    user_input = "".lower()
    while user_input == "":
        unchecked_input = input(question)

        # This checks to see if the user entered a number
        # If a number is entered, it is interpreted as the number printed alongside the options above

        if unchecked_input.isdigit():
            if int(unchecked_input)-1 in range(len(options)):
                return options[int(unchecked_input)-1]

        # This loop checks to see if any options begin with the input to allow short answers like "ye" instead of "yes"

        for y in options:
            if y.startswith(unchecked_input):
                return y

        # Only prints if none of the options begin with the user input

        if user_input == "":
            print("Please select one of the options provided")


test_question = "First time?"
test_options = ["yes", "no"]

# Prints instructions if yes, else no print

yes_or_no = multi_choice(test_question, test_options)
if yes_or_no == "yes":
    print(This is a program that will let you encrypt or decrypt a message using the Ceasar cipher and a key.)