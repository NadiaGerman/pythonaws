# Perfect Sociable Numbers Finder
# A sociable number is part of a sequence where the sum of the proper divisors loops back to the original number.
# This script checks for 4-member sociable sequences.

def sum_of_divisors(n):
    """Return the sum of proper divisors of n."""
    divisors = [1]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

def is_sociable(start, chain_length=4):
    """Check if a number starts a sociable chain of the given length."""
    sequence = []
    current = start
    for _ in range(chain_length):
        current = sum_of_divisors(current)
        if current in sequence:
            return False
        sequence.append(current)
    return sequence[-1] == start

# Check range (reduced for speed)
for i in range(100000, 2000000):
    if is_sociable(i, 4):
        print(f"Sociable sequence found starting at: {i}")
        break

