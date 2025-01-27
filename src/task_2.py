# Imagine a school that children attend for years. In each year, there are a certain number of groups started,
# marked with the letters. So if years = 7 and groups = 4For the first year, the groups are 1a, 1b, 1c, 1d, and for
#  the last year, the groups are 7a, 7b, 7c, 7d.

# Write a function that returns the groups in the school by year (as a string), separated with a comma and space in
# the form of "1a, 1b, 1c, 1d, 2a, 2b (....) 6d, 7a, 7b, 7c, 7d".

# Examples: csSchoolYearsAndGroups(years = 7, groups = 4) ➞
#  "1a, 1b, 1c, 1d, 2a, 2b, 2c, 2d, 3a, 3b, 3c, 3d, 4a, 4b, 4c, 4d, 5a, 5b, 5c, 5d, 6a, 6b, 6c, 6d, 7a, 7b, 7c, 7d"

# Notes:
# Assume all names start with a capital letter and are lowercase thereafter (i.e. don't worry about finding "BOB"
# or "bob").

def csWhereIsBob(names):
    for i in range(len(names)):
        if names[i] == "Bob":
            return i
    return -1
