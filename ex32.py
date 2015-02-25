# Loops and Lists

# Lists [Array]
hairs = ['black', 'brown', 'blond']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]

# For loops
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

"""
Syntax of for loops:
for [new_variable] in [defined_variable]:
"""
# This first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit

# We can also go through mixes of lists
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
"""
Python range - https://docs.python.org/2/library/functions.html#range
range(#1, #2, #3)
- start at #1 (include)
- end at #2 (don't include) 
- Step (Rate or addition of)
"""
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we print them out
for i in elements:
    print "Element was: %d" % i

"""
# The top two for loops can be put together to be one
for elements in range(0, 6):
    print "Elements was: %d" % elements
"""