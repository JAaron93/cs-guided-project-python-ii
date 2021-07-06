# Given a string of words, return the length of the shortest word(s).

# Notes:

# The input string will never be empty and you do not need to validate for different data types.

def csShortestWord(input_str):
    words = input_str.split()

    length = 100
    for w in words:
        if len(w) < length:
            length = len(w)

    return length
