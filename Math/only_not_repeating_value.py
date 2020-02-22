"""
Finds the only not repeating value in an array

given {1 2 3 1 2 3 4} -> 4
given {1 1 2 3 2 4 3} -> 4
"""

if __name__ == "__main__":
    arr = [1, 2, 3, 5, 1, 2, 3, 4, 4]

    remainder = 0b0

    for value in arr:
        remainder ^= value

    print(remainder)
