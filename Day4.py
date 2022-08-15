import hashlib

# # encoding GeeksforGeeks using md5 hash
# # function
# result = hashlib.md5(b"ckczppom1111111")
#
# # printing the equivalent byte value.
# print("The byte equivalent of hash is : ", end="")
# print(result)
# print(result.hexdigest())

number = 0
while True:
    input = f'ckczppom{str(number)}'
    result = hashlib.md5(bytes(input, 'utf-8'))
    hash = result.hexdigest()
    if hash[:6] == "000000":
        answer = number
        break
    number += 1
print(f"Answer is {number} with hash: {hash}")
