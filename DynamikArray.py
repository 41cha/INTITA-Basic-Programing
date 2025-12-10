import ctypes
import math

class DynamicArray:
    def __init__(self, start_capacity=8, growth_type="double"):
        self.capacity = start_capacity
        self.length = 0
        self.data = (self.capacity * ctypes.py_object)()
        self.growth_type = growth_type
        self.resize_count = 0

    def append(self, value):

        if self.length == self.capacity:
            self.resize()

        self.data[self.length] = value
        self.length += 1

    def resize(self):
        if self.growth_type == "double":
            growth = 2

        elif self.growth_type == "fixed":
            growth = 1 + 4 / 10

        elif self.growth_type == "dynamic":
            growth = 1 + (4 / 10) / math.log2(self.length + 2)

        else:
            growth = 2
        
        new_capacity = int(self.capacity * growth)

        if new_capacity <= self.capacity:
            new_capacity = self.capacity + 1

        new_data = (new_capacity * ctypes.py_object)()

        for i in range(self.length):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity
        self.resize_count += 1

    def get(self, index):

        if index < 0 or index >= self.length:
            raise IndexError("out of range")
        
        return self.data[index]

    def set(self, index, value):

        if index < 0 or index >= self.length:
            raise IndexError("out of range")
        
        self.data[index] = value

    def length_val(self):
        return self.length

    def print_all(self):

        for i in range(self.length):
            print(self.data[i], end=' -> ')

        print()

    def unused(self):
        return self.capacity - self.length
    
    def unused_persent(self):
        return round((self.capacity - self.length) / self.capacity * 100, 3)


arr = DynamicArray(8, "dynamic")

for i in range(25):
    arr.append(i)

arr.print_all() 

print("length:", arr.length_val())

print("item:", arr.get(3))

arr.set(3, 99)
 
print(arr.get(3))

print("resize count:", arr.resize_count)

print("unused:", arr.unused())

print(f"unused persent: {arr.unused_persent()} %")













# import ctypes
# import math

# class DynamicArray:
#     def __init__(self, initial_capacity=8, growth_factor=2):
#         self.capacity = initial_capacity
#         self.growth_factor = growth_factor
#         self.data = (self.capacity * ctypes.py_object)()
#         self.lenght = 0

#     def append(self, item):
#         if self.growth_factor == "log2":
#             new_capacity = int(self.capacity * math.log2(self.capacity))

#         else:
#             new_capacity = int(self.capacity * float(self.growth_factor))

#         new_data = (new_capacity * ctypes.py_object)()

#         for i in range(self.lenght):
#             new_data[i] = self.data[i]

#         self.data = new_data
#         self.capacity = new_capacity

#     def get(self, index):
#         if self.lenght <= index:
#             raise IndexError(f'index {index} out of range')
#         return self.data[index]


# import time
# sizes = [1, 10, 100, 1000, 10000, 100000, 1000000]
# for num in sizes:
#     arr = DynamicArray(8, log2)
#     t0 = time.time()
#     for i in range(num):
#         arr.append(i)
#     t1 = time.time()
#     print(f"Added {num} items in {t1-t0} seconds")
