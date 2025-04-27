# perfect and sociable numbers finder

def get_proper_divisors(n):
    """Returns a list of proper divisors of n (excluding n itself)."""
    return [i for i in range(1, n) if n % i == 0]

def is_perfect(n):
    """Checks if a number is perfect."""
    return sum(get_proper_divisors(n)) == n

def find_perfect_numbers(limit):
    """Finds and returns all perfect numbers up to a given limit."""
    return [x for x in range(2, limit) if is_perfect(x)]

# Example usage
if __name__ == "__main__":
    print("Perfect numbers under 10000:")
    print(find_perfect_numbers(10000))
