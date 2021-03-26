

flags = 0b10101

print(bin(flags))

print(bin(flags << 1))

print(bin(flags >> 1))

print(bin(flags | 0b01010))
print(bin(flags & 0b11110))
print(bin(flags ^ 0b11110))

print(bin(flags & 0b0))

print(2 << 6)

print(bin(flags & 0b0).rjust(10))
