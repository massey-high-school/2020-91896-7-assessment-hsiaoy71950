# This component only takes integers


def number_check():
    error = "That is not a cool number. You probably like decimals."
    number_loop = ""
    while number_loop == "":
        try:
            cool_number_input = input("Pop in a cool number (no decimals allowed!)")

            if float(cool_number_input) % 1 == 0:

                cool_number_input = int(cool_number_input)

                return cool_number_input
            else:
                print(error)
        except:
            print(error)


loop_de_loop = ""
while loop_de_loop == "":

    number = number_check()

    print("Yea {} is a pretty cool number".format(number))
