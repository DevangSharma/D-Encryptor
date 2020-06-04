message = "devang"
result = ""
key = "1111111111"

for i in range(0, 6):
    result += chr(ord('a') + (ord(message[i]) + int(key[i % 10])) % 97)
    print(ord(message[i]))

print("Your encrypted message is : ", result)
print("With Key : ", key)
