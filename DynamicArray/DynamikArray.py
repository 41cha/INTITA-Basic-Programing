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

    def lenght_val(self):
        return self.length

    def print_all(self):
        for i in range(self.length):
            print(self.data[i], end=' -> ')
        print()

    def unused(self):
        return self.capacity - self.length


