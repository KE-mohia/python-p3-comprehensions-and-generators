#!/usr/bin/env python3

def return_evens(sequence):
    return [num for num in sequence if num % 2 == 0]

# Test the function
result = return_evens([0, 1, 3, 5, 7, 8, 9])
print(result)  # Output: [0, 8]


def make_exclamation(sentences):
    return [sentence + '!' for sentence in sentences]

