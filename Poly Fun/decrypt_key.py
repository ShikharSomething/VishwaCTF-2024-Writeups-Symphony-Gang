from numpy.polynomial import Polynomial

with open("encoded_key.txt", "rb") as file:
    encrypted_key_data = file.read()
encrypted_key_str = encrypted_key_data.decode()
encrypted_key_nums = [ord(c) for c in encrypted_key_str]

key_nums = []
for num in encrypted_key_nums:
    poly = Polynomial([7 - num, 3, 4])
    roots = poly.roots()
    for root in roots:
        if root > 0:
            break
    key_nums.append(round(root))

key = bytes(key_nums)

print(key)
