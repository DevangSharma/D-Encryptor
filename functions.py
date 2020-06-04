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
    result = ""
    key = 1

    for letter in message:
        result += chr((ord(letter) + key % 26))

    print(result)
    print("\n", '*' * 100, '\n')
    print('your converted message is : \n',message,'\n')


def decrypt():
    print("You selected Decryption")
    message = input("Enter your message from line below :\n")


