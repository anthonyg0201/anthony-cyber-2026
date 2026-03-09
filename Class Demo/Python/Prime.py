#prime.py
#Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False  #Numbers less than 2 are not prime
    for i in range(2, n):
        if n % i == 0:
            return False # Found a divisor, not prime
    return True # No divisors found, number is prime

#Test the function
print(is_prime(7))  # Expected output: True
print(is_prime(10)) # Expected output: False

# Example of functwith default paramater
def greet(name="User"):
    print(f"Hello, {name}!")



greet()  #User default: Hello, User!
greet("Gavin")
