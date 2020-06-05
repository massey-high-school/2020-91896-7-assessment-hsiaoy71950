# This component only takes integers


def number_check():
    number_loop = ""
    while number_loop == "":
        cool_number_input = input("Pop in a cool number (no decimals allowed!)")

        # isdigit() doesn't allow negative signs and so by stripping all - signs on the left of the number it can be
        # preserved

        if cool_number_input.lstrip("-").isdigit():

            # eval used to allow unorthodox inputs like double negatives or equations

            return int(eval(cool_number_input))
        else:
            print("That is not a cool number. You ought to be ashamed of yourself. You probably like decimals.")


number = number_check()

# 72 because 72 is the coolest number and nobody can convince me otherwise

print("Yea {} is a pretty cool number but the number 72 is cooler".format(number))
