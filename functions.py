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


def decrypt():
    print("You selected Decryption")
    message = input("Enter your message from line below :\n")


