import string


def number_check():
    number_loop = ""
    while number_loop == "":
        cool_number_input = input("What key would you like to use? (Please enter a integer): ")

        # isdigit() doesn't allow negative signs and so by stripping all - signs on the left of the number it can be
        # preserved

        if cool_number_input.lstrip("-").isdigit():

            # eval used to allow unorthodox inputs like double negatives or equations

            return int(eval(cool_number_input))
        else:
            print("That is not a cool integer. You ought to be ashamed of yourself. You probably like decimals.")


def multi_choice(question, options):
    numbering = 0

    # Prints all the available options

    for x in options:
        numbering += 1
        print("{}.".format(numbering), x)
    user_input = ""
    while user_input == "":
        unchecked_input = input(question).lower()

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


yn_question = "Is this your first time using this program?: "
yn_options = ["yes", "no"]

yes_or_no = multi_choice(yn_question, yn_options)
if yes_or_no == "yes":
    print("This is a program that will let you encrypt or decrypt a message using the Caesar cipher and a key.")
else:
    print("Good luck!")


alphabet_string = string.ascii_lowercase
alphabet = []
for character in range(len(alphabet_string)):
    alphabet.append(alphabet_string[character])

    loop_whole_program = ""
    while loop_whole_program == "":
        crypt_question = "Would you like to encrypt or decrypt?: "
        crypt_options = ["decrypt", "encrypt"]
        choice = multi_choice(crypt_question, crypt_options)
        message = input("enter a message to be {}ed: ".format(choice)).lower()

        if message.islower():

            key = number_check()

            if key < 0:
                key %= -26
            else:
                key %= 26

            if choice == "decrypt":
                key = -key
            if key > 0:

                key += -26

            print("a --->", alphabet[alphabet.index("a") + key])

            string = ""

            for letters in message:
                if letters in alphabet:
                    string += alphabet[alphabet.index(letters) + key]
                else:
                    string += letters
            print(string)
        else:
            print("The message must contain letters!")
        loop_whole_program = input("press <enter> to end the program or any button to end it: ")