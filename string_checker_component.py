# This component only takes strings containing letters


def string_check():
    error = "That string has no letters because it is a fake"
    string_loop = ""
    while string_loop == "":
        string = input("Enter a string with letters!!!: ").lower()

        if string.islower():
            return string
        else:
            print(error)


loop_de_loop = ""
while loop_de_loop == "":

    text = string_check()

    print("Yea, \"{}\" contains letters".format(text))
