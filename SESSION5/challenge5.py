# Question 5: Working with Tuples

"""
Q13: Create a tuple animals with elements ("cat", "dog", "rabbit", "mouse").
Try to add "hamster" to the tuple. What happens?

Create a new tuple with this additional element.
"""

animals = ("cat", "dog", "rabbit", "mouse")
# Trying to add "hamster" to the tuple
# animals.append("hamster")  # This will raise an AttributeError

# Creating a new tuple with the additional element
animals = animals + ("hamster",)
print(animals)