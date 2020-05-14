from functions import *

print("Welcome! to D-Encryptor \nHere you can encode a message for someone else end at the other end one can decrypt "
      "it as well")

n = input("Press Enter to continue \n")

test_input(n,"")

print("Please select your task : \n 1 : Encryption \n 2 : Decryption")
task = int(input())
test_input_range(task,1,2)

 if(task - 1):
     decrypt()
 else :
    encrypt()
