# Question 3: Modifying Lists
"""
Q6: Change the second element of the fruits list to "blueberry".
Print the updated list.
"""
fruits = ["apple", "banana", "cherry", "date"]

print("Original list:")
print(fruits)

print("\nUpdated list to replacing banana by blueberry")
fruits[1] = "blueberry"
print(fruits)

# Q7: Add the fruit "elderberry" to the end of the fruits list. Print the updated list.
print("\nAdded the entry of elderberry by last element")
fruits.append("elderberry")
print(fruits)