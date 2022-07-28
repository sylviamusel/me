## Quiz revision!

## Keys and values of a dictionary

Getting something out of a dictionary

name_obj = person["name"] <- refers to the name key
title = name_obj["title"]

OR

person["name"]["title"]

person["interests"][0] <-looks into the first dictionary in the list

person["interests"][0]["name"][2]
= g
list("hello")
= H, E, L, L, O

To pull out a list [2]
To pull out from dict ["name"]

---

# IO stuff

. refers you are in
.. refers to a file back

utf-8 allows it to read and write all characters sets
f"{name} is cool and safe .... <- F string

read() <- reads everything as a string
readline() <- reads the first line, call again it reads the second line
readlines() <- reads as a list

import os
os.path.isfile(path_string)
\n\t <- n is a new line, t is a new tab

---

import random
for \_ in range(10)
print(random.randrange(0,4) <- print a random number between 0 & 3

     print(4 / random.randrange(0,4) <- divide by 4

expect ZeroDivisionError as z:
print("BOOM")

expect Exception as e: <- collects the error fast, try and find out
print(e)
