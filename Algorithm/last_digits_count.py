# Q2) Define a function that returns the frequencies of the last digits
#     of a list of nonnegative integers.
#
#     Use only the Python standard libraries.
#
#     Given the list [49, 10, 20, 5, 30, 785]:
#     9 is the last digit once (in 49),
#     0 is the last digit three times (in 10, 20 and 30),
#     5 is the last digit two times (in 5 and 785)
# last_digit_counts([49, 10, 20, 5, 30, 785])
#   = {9:1, 0:3, 5:2} # or something equivalent


def last_digit_counts(numbers):
    counts = {}
    # Explanation:
    # For each number in the list, we get the last digit by taking the modulus 10.
    # We then increment the count of that digit in the counts dictionary.
    for num in numbers:
        last_digit = num % 10
        counts[last_digit] = counts.get(last_digit, 0) + 1
    return counts


print(last_digit_counts([49, 10, 20, 5, 30, 785]))
