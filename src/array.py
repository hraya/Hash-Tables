# Lecture Notes

class DynamicArray:
    def __init__(self, capacity=8, ):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * capacity

    def insert(self, index, value):

        if self.count == self.capacity:
            self.double_size()

        for idx in range(self.count, index, -1):
            self.storage[idx] = self.storage[idx - 1]

        self.storage[index] = value
        self.count += 1

    def append(self, value):
        if self.count == self.capacity:
            self.double_size()

        self.storage[self.count] = value
        self.count += 1

    def double_size(self):
        self.capacity = self.capacity * 2
        new_arr = [None] * self.capacity
        for i in range(self.count):
            new_arr[i] = self.storage[i]
        self.storage = new_arr


# instructor notes below
# import time
# ​
# class DynamicArray:
#     def __init__(self, capacity=8):
#         self.capacity = capacity
#         self.count = 0
#         self.storage = [None] * capacity
# ​
# ​
#     def insert(self, index, value):
# ​
#         if self.count == self.capacity:
#             self.double_size()
# ​
#         for idx in range(self.count, index, -1):
#             self.storage[idx] = self.storage[idx - 1]
# ​
#         self.storage[index] = value
#         self.count += 1
# ​
#     def append(self, value):
#         if self.count == self.capacity:
#             self.double_size()
# ​
#         self.storage[self.count] = value
# ​
#         self.count += 1
# ​
#     def double_size(self):
#         # double the capacity
#         self.capacity = self.capacity * 2
#         # make a new array twice the size of the old one
#         new_arr = [None] * self.capacity
# ​
#         # copy everything over
#         for i in range(self.count):
#             new_arr[i] = self.storage[i]
# ​
#         self.storage = new_arr
# ​
# # O(n^2)
# def add_to_front(n):
#     x = []
#     for i in range(n):
#         x.insert(i, n-1)
#     return x
# ​
# # O(n)
# def add_to_back(n):
#     x = []
#     for i in range(n):
#         x.append(i)    # between friends we say this is O(1) even though sometimes we have to resize
#     return x
# ​
# ## Let's NEVER resize! bwahahaha
# def preallocate(n):
#     x = [None] * n
# ​
#     for i in range(n):
#         x[i] = i
# ​
#     return x
# ​
# n = 10000000
# start_time = time.time()
# add_to_front(n) # O(n^2)
# end_time = time.time()
# ​
# print("Time to add to front", end_time - start_time)
# ​
# start_time = time.time()
# add_to_back(n) # O(n)
# end_time = time.time()
# ​
# print("Time to add to back", end_time - start_time)
# ​
# start_time = time.time()
# preallocate(n) # O(n)
# end_time = time.time()
# ​
# print("Time to add to back, if we preallocate space", end_time - start_time)