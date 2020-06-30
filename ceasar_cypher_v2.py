import string
from random import randint
from collections import Counter


def number_check():
    number_loop = ""
    while number_loop == "":
        number_input = input("What key would you like to use? (Please enter a integer): ")
        print()

        if number_input == "":
            return "blank"

        # isdigit() doesn't allow negative signs and so by stripping all - signs on the left of the number it can be
        # preserved

        if number_input.lstrip("-").isdigit():
            return int(number_input)
        else:
            error_printer("!! Please only enter integers !!")
            print()


def multi_choice(question, options):

    numbering = 0
    error = "!! Please select one of the options provided !!"

    print(border)

    # Prints all the available options

    for num in options:
        numbering += 1
        print("{}.".format(numbering), num)
    user_input_loop = ""
    while user_input_loop == "":
        print()
        unchecked_input = input(question).lower()

        # This checks to see if the user entered a number
        # If a number is entered, it is interpreted as the number printed alongside the options above

        if unchecked_input.isdigit():
            if int(unchecked_input)-1 in range(len(options)):
                return options[int(unchecked_input)-1]

        if unchecked_input == "":
            print()
            error_printer(error)
        else:

            # This loop checks to see if any options begin with the input to allow short answers like
            # "ye" instead of "yes"

            for y in options:
                if y.startswith(unchecked_input):
                    return y
            print()

            error_printer(error)


# Split key and choice function into two

def choose_decrypt_encrypt():
    picked_option = multi_choice(crypt_question, crypt_options)
    print()
    return picked_option


def key_picker():
    picked_number = number_check()

    # this part allows for blank inputs
    # blank for encrypting results in a random key being generated
    # blank for decrypting results in returning a special function that will make the program loop with
    # frequency analysis

    if picked_number == "blank":
        if choice == "encrypt":
            picked_number = randint(1, 25)
        else:
            leave_blank_guess = multi_choice("Leaving this blank will print out all "
                                             "possible options from most likely to least "
                                             "likely. Are you sure you want to continue?", yn_options)
            if leave_blank_guess == "yes":
                return "guess key"
            else:
                picked_number = key_picker()
                return picked_number

    if picked_number < 0:
        picked_number %= -26
    else:
        picked_number %= 26

    if choice == "decrypt":
        picked_number = -picked_number
    if picked_number > 0:
        picked_number += -26
    return picked_number


def perform_encrypt(text, number):
    # Iterates through every character in the message entered and if the
    # character is a letter, it will be
    # cycled through the alphabet list to encrypt/decrypt it and appends the character to a string

    encrypted_string = ""

    for letters in text:
        if letters in alphabet:
            encrypted_string += alphabet[alphabet.index(letters) + number]
        else:
            encrypted_string += letters
    print("{}ed message: {}".format(choice, encrypted_string))


def error_printer(error_message):
    print("!" * len(error_message))
    print(error_message)
    print("!" * len(error_message))


# Declaring options and questions before the loop so they they aren't pointlessly redefined

yn_question = "Is this your first time using this program?: "
yn_options = ["yes", "no"]
crypt_question = "Would you like to encrypt or decrypt?: "
crypt_options = ["encrypt", "decrypt"]
end_question = "What do you want to do now?: "
border = "-" * 72
key_blank = ""

# alphabet in order of most frequent letters to least frequent for frequency analysis

frequency_list = ["e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p", "b",
                  "v", "k", "j", "x", "q", "z"]

# prints instructions if it is the first time the user is using the program

yes_or_no = multi_choice(yn_question, yn_options)
print(border)
if yes_or_no == "yes":
    print("This is a program that will let you encrypt or decrypt a message using \n"
          "the Caesar cipher and a key.\n\n"
          "The Caesar cipher works by shifting all letters in a message as many\n"
          "spaces as the key specifies. For example, a key of 1 will shift the\n"
          "letter A one place forward ans so A will become B and if the key\n"
          "is 2, A will become C and so on.\n\n"
          "With this program, you can automatically encrypt a message with a\n"
          "key.\n\nIf no key is provided, one will be randomly generated for you and\n"
          "the randomly generated key will be given to you.\n\n"
          "This program can also decrypt an encrypted message. If the key is\n"
          "unknown, all possible decrypted messages will be printed, using\n"
          "frequency analysis to sort them from most likely to least likely.\n")
else:
    print("Good luck!")

# creates a list containing the alphabet to cycle through when encrypting/decrypting later on

alphabet_string = str(string.ascii_lowercase)
alphabet = []
for character in alphabet_string:
    alphabet.append(character)

choice = choose_decrypt_encrypt()
key = key_picker()

loop_whole_program = ""
while loop_whole_program == "":

    message_check_loop = ""
    while message_check_loop == "":

        # Checks to see if the message entered contains letters so that the encryption/decryption isn't pointless

        message = input("enter a message to be {}ed: ".format(choice)).lower()

        if message.islower():

            print(border)

            key_blank = "false"

            if key == "guess key":

                key_blank = "blank"

                for x in frequency_list:

                    frequency_index = alphabet.index(x)

                    common_letter = alphabet.index(Counter(message).most_common(1)[0][0])

                    key = frequency_index - common_letter
                    if key > 0:
                        key -= 26

                    # Prints what the letter "a" will become after encryption or decryption

                    print("a --->", alphabet[alphabet.index("a") + key])

                    # Prints key used to show user what key was used. Useful when key was randomly picked

                    used_encryption_key = -key

                    print("key used: {}".format(used_encryption_key))

                    perform_encrypt(message, key)

                    print()

            else:

                # Prints what the letter "a" will become after encryption or decryption

                print("a --->", alphabet[alphabet.index("a") + key])

                # Prints key used to show user what key was used. Useful when key was randomly picked

                if choice == "encrypt":
                    used_encryption_key = 26 + key
                else:
                    used_encryption_key = -key

                print("key used: {}".format(used_encryption_key))

                perform_encrypt(message, key)
            message_check_loop = 1
        else:
            error_printer("!! The message must contain letters !!")

    # Because my option checker works by checking for the first letters of the option, the end options could
    # start with the same letters if encrypt is selected (e.g: 2. encrypt again... 3. encrypt/decrypt...)
    # this would not be good as the user could enter encrypt and it will not be interpreted as option 3 since the
    # function checks by iterating through the option list and will see 2 as a match first.
    # I avoided this by changing the option to encrypt/decrypt decrypt is selected and decrypt/encrypt when encrypt is
    # selected as they will no longer start with the same characters.

    if choice == "decrypt":
        not_choice = "encrypt"
    else:
        not_choice = "decrypt"

    # Must be put down here for .format to function correctly

    # first option edited to make intent more clear
    # added option to do the opposite task with same key

    if key_blank == "blank":
        end_options = ["Stop the program", ("{}/{} with a different key".format(not_choice, choice)).capitalize()]
    else:
        end_options = ["Stop the program", ("{} another message with the same key".format(choice)).capitalize(),
                       ("{}/{} with a different key".format(not_choice, choice)).capitalize(),
                       "Use the same key to {} a message".format(not_choice)]

    end_program_option = multi_choice(end_question, end_options)
    if end_program_option == "Stop the program":
        loop_whole_program = 1
    elif end_program_option == ("{}/{} with a different key".format(not_choice, choice)).capitalize():
        choice = choose_decrypt_encrypt()
        key = key_picker()

    elif end_program_option == "Use the same key to {} a message".format(not_choice):
        key = -key
        if key > 0:
            key -= 26
        choice = not_choice
    print(border)
