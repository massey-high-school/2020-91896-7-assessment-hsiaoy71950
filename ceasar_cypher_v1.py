import string


def number_check():
    number_loop = ""
    while number_loop == "":
        cool_number_input = input("What key would you like to use? (Please enter a integer): ")

        # isdigit() doesn't allow negative signs and so by stripping all - signs on the left of the number it can be
        # preserved

        if cool_number_input.lstrip("-").isdigit():
            return int(cool_number_input)
        else:
            print("That is not a cool integer. You ought to be ashamed of yourself. You probably like decimals.")


def multi_choice(question, options):
    numbering = 0
    error = "Please select one of the options provided"

    # Prints all the available options

    for x in options:
        numbering += 1
        print("{}.".format(numbering), x)
    user_input_loop = ""
    while user_input_loop == "":
        unchecked_input = input(question).lower()

        # This checks to see if the user entered a number
        # If a number is entered, it is interpreted as the number printed alongside the options above

        if unchecked_input.isdigit():
            if int(unchecked_input)-1 in range(len(options)):
                return options[int(unchecked_input)-1]

        if unchecked_input == "":
            print(error)
        else:

            # This loop checks to see if any options begin with the input to allow short answers like
            # "ye" instead of "yes"

            for y in options:
                if y.startswith(unchecked_input):
                    return y
            print(error)


# Condenses asking for decrypt/encrypt and the key into one function as this is used multiple times in the main program

def key_choice():
    global choice
    global key
    choice = multi_choice(crypt_question, crypt_options)
    key = number_check()

    if key < 0:
        key %= -26
    else:
        key %= 26

    if choice == "decrypt":
        key = -key
    if key > 0:
        key += -26


# Declaring options and questions before the loop so they they aren't pointlessly redefined

yn_question = "Is this your first time using this program?: "
yn_options = ["yes", "no"]
crypt_question = "Would you like to encrypt or decrypt?: "
crypt_options = ["decrypt", "encrypt"]
end_question = "What do you want to do now?: "

choice = ""
key = 0

# prints instructions if it is the first time the user is using the program

yes_or_no = multi_choice(yn_question, yn_options)
if yes_or_no == "yes":
    print("This is a program that will let you encrypt or decrypt a message using the Caesar cipher and a key.")
else:
    print("Good luck!")

# creates a list containing the alphabet to cycle through when encrypting/decrypting later on

alphabet_string = str(string.ascii_lowercase)
alphabet = []
for character in alphabet_string:
    alphabet.append(character)

key_choice()

loop_whole_program = ""
while loop_whole_program == "":

    message_check_loop = ""
    while message_check_loop == "":

        # Checks to see if the message entered contains letters so that the encryption/decryption isn't pointless

        message = input("enter a message to be {}ed: ".format(choice)).lower()

        if message.islower():

            # Prints what the letter "a" will become after encryption or decryption

            print("a --->", alphabet[alphabet.index("a") + key])

            # Iterates through every character in the message entered and if the character is a letter, it will be
            # cycled through the alphabet list to encrypt/decrypt it and appends the character to a string

            string = ""

            for letters in message:
                if letters in alphabet:
                    string += alphabet[alphabet.index(letters) + key]
                else:
                    string += letters
            print(string)
            message_check_loop = 1
        else:
            print("The message must contain letters!")

    # Because my option checker works by checking for the first letters of the option, the end options could
    # start with the same letters if encrypt is selected (e.g: 2. encrypt again... 3. encrypt/decrypt...)
    # this would not be good as the user could enter encrypt and it will not be interpreted as option 3 since the
    # function checks by iterating through the option list and will see 2 as a match first.
    # I avoided this by changing the option to encrypt/decrypt decrypt is selected and decrypt/encrypt when encrypt is
    # selected as they will no longer start with the same characters.

    if choice == "decrypt":
        not_choice = "Encrypt/decrypt"
    else:
        not_choice = "Decrypt/encrypt"

    # Must be put down here for .format to function correctly

    end_options = ["Stop the program", ("{} again with the same key".format(choice)).capitalize(),
                   "{} with a different key".format(not_choice)]

    end_program_option = multi_choice(end_question, end_options)
    if end_program_option == end_options[0]:
        loop_whole_program = 1
    elif end_program_option == end_options[2]:
        key_choice()
