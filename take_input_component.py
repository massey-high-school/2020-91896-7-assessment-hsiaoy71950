# This component prints all the choices given to the user and makes them enter a valid option


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


test_question = "decrypt or encrypt?: "
test_options = ["decrypt", "encrypt"]
loop_de_loop = ""
while loop_de_loop == "":
    decrypt_encrypt = multi_choice(test_question, test_options)
    message = input("please enter a {}ed message".format(decrypt_encrypt))
    print("I would {} but I have no key and I must {}.".format(decrypt_encrypt, decrypt_encrypt))
