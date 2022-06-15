"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think it will declare a variable called some_words
# It'll put a list of strings into it
some_words = ["what", "does", "this", "line", "do", "?"]

# I think it will loop over a list of words and therfore print the word which is next in the list
for word in some_words:
    print(word)

# I think it will do the same as line 22-24. the variable 'x' and 'word' are the same
for x in some_words:
    print(x)

# I think this will print the entire list
print(some_words)

# I think it will print ("some_words contains more than 3 words") as the list has more than 3 items/words in that list
if len(some_words) > 3:
    print("some_words contains more than 3 words")

# I think that this will print information about my computer (system, node, release, version, machine, and processor)
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())


usefulFunction()
