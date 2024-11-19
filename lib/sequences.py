#!/usr/bin/env python3

def print_fibonacci(length):

    # Initialize the first two numbers of the sequence
    fibonacci_sequence = [0, 1]

    # Generate the sequence up to the specified length
    while len(fibonacci_sequence) < length:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)

    # Print the sequence up to the desired length
    print(fibonacci_sequence[:length])