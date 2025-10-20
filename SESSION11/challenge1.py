# Challenge 1

"""
Write a program that will ask the user for five of his favorite activites
from most preferred to least preffered for example:
"Cycling", "Watching Movies", "Eating out", "Driving to work", "Doing a night class on Tuesday"
Save a file called activities.txt for those
Provide the user with a confirmation message that the inputs are being saved
Read from the saved file and print them in the console
"""

# Example to write example activities to a file and read them back

activities = ["Cycling", "Watching Movies", "Eating out",
              "Driving to work", "Doing a night class on Tuesday"]
with open("activities.txt", "w") as file:
    for activity in activities:
        file.write(activity + "\n")
file.close()
print("Example favorites activities has been saved to activities.txt")

with open("activities.txt", "r") as file:
    saved_activities = file.readlines()
    print("Here are the example activities:")
    for activity in saved_activities:
        print(activity.strip())
file.close()