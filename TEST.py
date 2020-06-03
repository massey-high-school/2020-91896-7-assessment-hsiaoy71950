# super simple mock up

choice = input("decrypt or encrypt?")
message = input("enter message")
key = int(input("put in a key"))

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]

if key < 0:
    remainder = key % -26
else:
    remainder = key % 26

if choice == "decrypt":
    key = (-26) - remainder
else:
    key = (-26) + remainder

print("a --->", alphabet[alphabet.index("a") + key])

string = ""

for x in message:
    if x in alphabet:
        string += alphabet[alphabet.index(x) + key]
    else:
        string += x
print(string)
