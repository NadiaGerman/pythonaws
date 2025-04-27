
def fibonacci(n):
    """Generate a list containing the Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    sequence = [0]
    if n > 1:
        sequence.append(1)
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Testing the function
print("Fibonacci (5 terms):", fibonacci(5))
print("Fibonacci (10 terms):", fibonacci(10))
print("Fibonacci (1 term):", fibonacci(1))
print("Fibonacci (0 terms):", fibonacci(0))
