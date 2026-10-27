import math

total_keys = math.factorial(25)

print("Total possible keys:", total_keys)
print("Approximate power of 2:", math.log2(total_keys))
print("Approximate number of bits:", round(math.log2(total_keys)))