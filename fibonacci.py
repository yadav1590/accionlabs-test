class FibonacciSumCalculator:
    def __init__(self):
        self.even_fib_sum = 0  
        self.even_fib_count = 0  
        self.fib1 = 0  # First Fibonacci number (F(0))
        self.fib2 = 1  # Second Fibonacci number (F(1))

    def generate_fibonacci(self):
        """Generate Fibonacci numbers and calculate the sum of even ones."""
        while self.even_fib_count < 100:  # We only need the first 100 even Fibonacci numbers
            # Calculate the next Fibonacci number
            next_fib = self.fib1 + self.fib2
            self.fib1 = self.fib2
            self.fib2 = next_fib

            # Check if the Fibonacci number is even
            if next_fib % 2 == 0:
                self.even_fib_sum += next_fib
                self.even_fib_count += 1

    def get_even_fib_sum(self):
        """Return the sum of the first 100 even Fibonacci numbers."""
        return self.even_fib_sum


# Usage Example:

if __name__ == "__main__":
    # Instantiate the FibonacciSumCalculator
    calculator = FibonacciSumCalculator()
    
    # Generate Fibonacci numbers and sum the even ones
    calculator.generate_fibonacci()
    
    # Output the result
    print("Sum of the first 100 even Fibonacci numbers:", calculator.get_even_fib_sum())
