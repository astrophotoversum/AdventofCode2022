"""
This is the script for the 1st door of AOC 2022
"""

"""
For the first riddle
"""
# The input is copied into a txt-file named input.txt. This file is opened here.
file = open('input.txt', 'r')

# Each line is read
Lines = file.readlines()
file.close()

# This variable is used to temporarly store the calories of each individual elve
elvesum = []

# In the for loop every calorie-sum is append to the list "calorielist". this list will contain the summed calories of all elves
calorielist = []


for line in Lines:

    # If an emtpy line in the file is found during a cycle in the loop all calories carried by one elf are summed and append to the total calorielist.
    if line == '\n':
        # An empty line was found so the sum of the calories for this individual elf is taken and appended to the total calorielist
        calorielist.append(sum(elvesum))
        # To ensure that only the individual calories are summed the elvesum-list is cleared as soon as an emtpy line is found.
        elvesum = []
        continue

    # Append the calorie value the list.
    elvesum.append(int(line))

# The maximum of the calorielist is the answer to the riddle ()
print("The elf carrying the most calories, carries "+ str(max(calorielist)) + " calories. \n")

"""
For the second riddle
"""
# Sort the carried calories in descending order
calorielist_sorted = sorted(calorielist, reverse=True)

# Since we want the first three elves we index from 0 to 3 (excluded)
top3_calories = calorielist_sorted[0:3]

# Take the sum
top3_sum = sum(top3_calories)
# Print the answer
print("The 3 elves carrying the most calories, carry " + str(top3_sum) + " calories together.")