class FibonacciSeries:
    def __init__(self, n):
        self.n = n  # Number of terms in the Fibonacci series
    
    def generate_series(self):
        fib_series = []
        a, b = 0, 1  # First two terms of the Fibonacci series
        
        for _ in range(self.n):
            fib_series.append(a)
            a, b = b, a + b  # Update the values of a and b to the next terms in the series
        
        return fib_series

    def display_series(self):
        series = self.generate_series()
        print(f"Fibonacci series up to {self.n} terms:")
        print(series)

# Example usage
if __name__ == "__main__":
    try:
        n = int(input("Enter the number of terms for the Fibonacci series: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            fib_series = FibonacciSeries(n)
            fib_series.display_series()
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
