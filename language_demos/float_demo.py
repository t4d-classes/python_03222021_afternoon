import sys
import math
from decimal import Decimal

# num_1 = 0.1 + 0.2
# num_2 = 0.3

# print(num_1)
# print(num_2)

# print(num_1 == num_2)

# # print(abs(num_1 - num_2) < sys.float_info.epsilon)
# print(math.isclose(num_1, num_2))

num_1 = Decimal("0.1") + Decimal("0.2")
num_2 = Decimal("0.3")

print(num_1)
print(num_2)

print(num_1 == num_2)
