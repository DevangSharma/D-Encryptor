from random import randint

def test_input(n, chk):
    while True:
        if n == chk:
            print("\n", '*' * 100, "\n")
            break

        else:
            print("Wrong key pressed, Try again\n")
            n = input()


def test_input_range(n, chk1, chk2):
    while True:
        if n >= chk1 or n <= chk2:
            print("\n", '*' * 100, "\n")
            break

        else:
            print("Wrong input , Try again\n")
            n = input()


def encrypt():
    print("You selected Encryption")
    message = input("Enter your message from line below :\n")
    message = message.lower()
    l = len(message)

    result = ""
    key = str(randint(0,9999999999))

    for i in range(0, l):

        if (message[i] == ' '):
            result += "."
        else:
            result += chr(ord('a') + (ord(message[i]) + int(key[i % 10])) % 97)

    print("Your encrypted message is : ", result)
    print("With Key : ", key)

    print("\n", '*' * 100, '\n')


def decrypt():
    print("You selected Decryption")
    message = input("Enter your message from line below :\n")
    key = input("Enter your key : ")

    result = ""
    l = len(message)

    for i in range(0, l):

        if(message[i] == '.'):
            result += " "
        else:
            result += chr(ord('a') + (ord(message[i]) - int(key[i % 10])) % 97)

    print(result)




