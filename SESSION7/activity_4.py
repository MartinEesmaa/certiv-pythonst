# Shadowing

"""
Variable shadowing occurs when a variable declared within
a certain scope (decision block, method or inner class) has the
same name as a variable declared in an outer scope.
"""

# global
name = "tom"
def hello_name(name):
    # local
    print('hello {}'.format(name))
print(name)
hello_name('john')
# Output:
# tom // global
# hello john // local