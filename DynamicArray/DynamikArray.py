import ctypes
import math
import time
import matplotlib.pyplot as plt


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

growth_types = ["double", "fixed", "dynamic"]
sizes = [100, 1000, 5000, 10000, 50000, 100000]
results = {gt: [] for gt in growth_types}

for growth_type in growth_types:
    times = []
    for num in sizes:
        arr = DynamicArray(8, growth_type=growth_type)
        t0 = time.time()

        for i in range(num):
            arr.append(i)

        t1 = time.time()
        times.append((t1 - t0) * 1000)  # в мілісекунди

    results[growth_type] = times

plt.figure(figsize=(10, 6))

for growth_type in growth_types:
    plt.plot(sizes, results[growth_type], marker='o', label=growth_type, linewidth=2)

plt.xlabel('Кількість елементів')
plt.ylabel('Час додавання (мс)')
plt.title('Порівняння швидкості DynamicArray для різних growth_type')
plt.legend()

plt.grid(True, alpha=0.3)
plt.yscale('log') 
plt.xticks(sizes)
plt.tight_layout()
plt.show()
