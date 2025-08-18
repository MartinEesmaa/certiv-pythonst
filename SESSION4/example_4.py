# More examples of break statement

# First example
for letter in 'Python':
    if letter == 'h':
        break
    print("Current Letter :", letter)

# Second example
var = 10
while var > 0:
    print('Current variable value :', var)
    var = var - 1
    if var == 5:
        break
    print("Good bye!")