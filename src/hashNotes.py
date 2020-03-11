# hash lecture notes

import hashlib
import time


# Below simple example of hash function
def myFakeHash(word):
    hash = len(word)
    return hash

myFakeHash("Timothy") # --> 7
myFakeHash("sevenns") # --> 7

# Avoid collisions

# scramble the key and come up with very different values
def djb2(key):
    # start from a large prime number
    hash_value = 5381

    # randomly scramble it by bit-shifting
    for char in key:
        hash_value = hash_value + (hash_value << 5) + char

    return hash_value

# hashlib.sha256()

# example of hash functions
key = b"mypassword"

n = 10000
start_time = time.time()
for i in range(n):
    djb2(n)
end_time = time.time()

print("djb2 run time: ", end_time - start_time)

start_time = time.time()
for i in range(n):
    hashlib.sha256(key)
end_time = time.time()

print("sha256 run time: ", end_time - start_time)

start_time = time.time()
salt = bcrypt.gebsalt()
for i in range(n):
    bcrypt.hashpw(key, salt)
end_time = time.time()

print("hashpw run time: ", end_time - start_time)

# instructor notes below
# import time
# import hashlib
# import bcrypt
​
# hash("myname") ---> "0abcd8278ef8ab8e"
​
# Deterministic: For a given input, the output will always be the same.
# Defined output range: For a hash table of size 16, all keys must hash to a value 0-15. For smaller values, this is usually accomplished using the modulo % operation.
# Predictable Speed: Hash functions for hash tables should be lightning fast while cryptographic hashes (like bcrypt) should be very slow.
# Non-invertible: You should not be able to reconstruct the input value from the output. This trait is important in cryptographic hashes but not necessary for general hash tables.
​
# Avoid collisions
​
# def myFakeHash(word):
#     hash = len(word)
#     return hash
# ​
# myFakeHash('Timothy') # --> 7
# myFakeHash('sevenns') # --> 7
# ​
# ​
# # scramble the key and come up with very different values
# def djb2(key):
#     # start from a large prime number
#     hash_value = 5381
# ​
#     # randomly scramble it by using bit-shifting
#     for char in key:
#         hash_value = hash_value + (hash_value << 5) + char
# ​
#     return hash_value
# ​
# ​
# key = b"mypassword"
# ​
# n = 10000
# ​
# start_time = time.time()
# for i in range(n):
#     djb2(key)
# end_time = time.time()
# ​
# print("djb2 run time: ", end_time - start_time)
# ​
# ​
# start_time = time.time()
# for i in range(n):
#     hashlib.sha256(key)
# end_time = time.time()
# ​
# print("sha256 run time: ", end_time - start_time)
# ​
# start_time = time.time()
# salt = bcrypt.gensalt()
# for i in range(n):
#     bcrypt.hashpw(key, salt)
# end_time = time.time()
# ​
# print("hashpw run time: ", end_time - start_time)