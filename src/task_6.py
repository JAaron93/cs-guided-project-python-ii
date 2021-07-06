# Given a start integer and an ending integer (both inclusive), write a function that returns the count (not the sum)
#  of all integers in the range (except integers that contain the digit 5).

# Examples:

# csAnythingButFive(1, 5) -> 1, 2, 3, 4, -> 4 (there are 4 integers in the range that do not contain the digit 5)
# csAnythingButFive(1, 9) -> 1, 2, 3, 4, 6, 7, 8, 9 -> 8
# csAnythingButFive(4, 17) -> 4,6,7,8,9,10,11,12,13,14,16,17 -> 12
# Notes:

# The output can contain the digit 5.
# The start number will always be less than the end number (both numbers can also be negative).


def csAnythingButFive_str(start, end):
    ''' With a string conversion'''
    count = 0
    for i in range(start, end + 1):
        if "5" not in str(i):
            count += 1
    return count


def csAnythingButFive(start, end):
    '''Without string conversion'''
    output = [i for i in range(start, end+1)]
    counter = 0
    for i in output:
        if (i in range(50, 60)) or ((i % 5 == 0) and (i % 2 != 0)):
            counter += 1
    return (len(output) - counter)
