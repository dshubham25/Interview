# For a given positive number N in base-10, return the complement of its binary representation as a base-10 integer

def calculate_bitwise_complement(num):
    bit, n = 0, num
    while n > 0:
        bit += 1
        n = n >> 1
    all_bitset = pow(2, bit) - 1
    return num ^ all_bitset


print(calculate_bitwise_complement(8))
print(calculate_bitwise_complement(11))
