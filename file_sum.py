# Hieu Ngo
# 10/26/2020
# Assignment 5a - Write a function that takes a file as a parameter
# then sums up all the numbers inside then returns the sum.

def file_sum(filename):
    """Sums up all of the numbers in a text file then writes the sum in a new file."""
    sum = 0
    with open(filename, 'r') as infile:
        for line in infile:
            number = line.strip()
            sum += float(number)

    with open('sum.txt', 'w') as outfile:
        str_sum = str(sum)
        outfile.write(str_sum)

#file_sum('numbers.txt')