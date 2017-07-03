"""
function that takes one argument and generates a list of prime numbers up to that argument
"""


def prime_number(number):
    # Check if argument is an integer
    if isinstance(number, int):
        # Check if argument is a positive integer
        if number > 0:
            number_set = set(range(2, number))
            prime_numbers = []
            # iterate while number set isn't empty
            while number_set:
                num = number_set.pop()
                prime_numbers.append(num)
                number_set.difference_update(set(range(num * 2, number + 1, num)))
            return prime_numbers
        else:
            # return empty list if the argument is a negative integer
            return []
    else:
        # raise a value error if argument is not an integer
        raise ValueError("Argument must be an integer")
