# bugCollector.py
# Grant Andrews
# 2/25/22
# This program allows a user to enter the names of bugs that were caught on five different days
# from a predetermined list of bug names. The program keeps a tally of the bugs caught and tells
# the user how many bugs were caught in total across all five days


# initialize variables and create a list
day, bugs, bug_count = 1, 0, 0
bug_names = ["holly blue", "emperor moth", "orange-tip", "ruby tiger moth", "brimstone", "streamer moth", "speckled wood", "purple thorn moth",
             "peacock"]

# tell the user how the program works, which bug names they may enter and how to do so
print("This program counts the number of bugs caught during a five day period. The acceptable bug names are as follows :")
print(*bug_names, sep=", ")
print("The bug names must be spelled correctly in order to be counted, the bug names are not case sensitive.\n\
\nPlease enter the bugs you caught on each day. Write 'done' to proceed to the next day: ")

# this for loop will run 5 times, each time it reinitializes the variable 'bugs', and prints
# to the user which day they are on
for day in range(1, 6):
    bugs = 0
    print("Day: ", day)

    # this while loop will continue to run until the user inputs "done"
    # when "done" is entered, a value of '1' is added to the variable 'day'
    # and the while loop breaks and passes back to the for loop
    # when a valid bug name is entered, it adds a value of '1' to the variable 'bug_count'
    # if an invalid bug name is entered, the user is informed that the bug was not counted 
    while bugs != "done":
        bugs = input().lower()
        if any(x in bugs for x in bug_names):
            bug_count += 1
        if bugs not in (bug_names) and bugs != "done":
            print("Invalid input, bug not counted!")
        if bugs == "done":
            day += 1
            break

# prints the number of bug caught
print("Total number of bugs that you caught is:", bug_count)
