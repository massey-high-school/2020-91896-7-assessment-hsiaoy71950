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


crypt_question = "decrypt or encrypt?: "
crypt_options = ["decrypt", "encrypt"]
choice = multi_choice(crypt_question, crypt_options)
message = input("enter a message to be {}ed.".format(choice))
key = number_check()

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]

if key < 0:
    remainder = key % -26
else:
    remainder = key % 26

if key > 0:
    key = (-25 + key)

print("a --->", alphabet[alphabet.index("a") + key])

string = ""

for x in message:
    if x in alphabet:
        string += alphabet[alphabet.index(x) + key]
    else:
        string += x
print(string)
