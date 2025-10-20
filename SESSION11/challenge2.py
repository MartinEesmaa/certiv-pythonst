# Challenge 2

"""
Write a program that will read the activities.txt
and then write the activities in a reverse order
to another file named 'reverse.txt'. And then close the file.
"""

with open("activities.txt", "r") as file:
    activities = file.readlines()
    activities = [activity.strip() for activity in activities]
    activities.reverse()
with open("reverse.txt", "w") as file:
    for activity in activities:
        file.write(activity + "\n")
file.close()