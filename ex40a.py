mystuff = {'apple': "I AM APPLES!"}
#print(mystuff['apple'])

# this goes in mystuff.py
#def apple():
#    print("I AM APPLES!")

#import mystuff
import mystuff2
mystuff2.apple()
#print(mystuff.apple)
#mystuff.tangerine()
print(mystuff2.tangerine)

# this is how you call from a dict
mystuff['apple'] # this calls the dict in line 1 
# this is how you call from a module
mystuff2.apple() # this calls a module defined on line 9
mystuff2.tangerine # same thing, it's just a variable

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")clear
        

#thing = MyStuff()
#thing.apple()
#print(thing.tangerine)

# dict style
#mystuff['apples']

# module style
#mystuff.apples()
#print(mystuff.tangerine)

# class style
#thing = MyStuff()
#thing.apples()
#print(thing.tangerine)
