#!/usr/bin python

the_count =[1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

#same as above
for fruit in fruits:
    print "fruits: %s" % fruit

#also we can go through mixed lists too
#notice we have to use #r since we don't know what's in it <-----------!

for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
""" original
for i in range(0, 6):
    print "Adding %d to the list." %i
    #append is a function that lists
    elements.append(i)
    print elements

for i in elements:
    print "Each item in elements: %d" %i
"""

#alt for the above
#elements.append(0,1,2,3,4,5)
#print elements

#print fruits[1]







