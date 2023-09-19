import os

# r - Read
# a - Append
# w - Write
# x - Create

# READ - error if it doesn't exist

f = open("names.txt")
# print(f.read()) # - reading the entire file
# print(f.read(10)) # - reading the first 10 characters
# print(f.readline()) # - reading the first line within file

# looping through each line in a file:
for line in f:
    # print(line)
    pass

f.close() # we always have to close the file after we opened it, otherwise changes won't impact the file

# APPEND - creates the file if it doesn't exist
f1 = open("names.txt", "a")
f1.write("""
    Ismoil
    Sorbon
    Somon
    Umed
    Buzurg
    Muhammad
    Bahodur
    Saidkamol
    Abdullo
""")

f1 = open("names.txt")
# print(f1.read())
f1.close()

# WRITE - overwrites the file
f2 = open("names.txt", "w")
f2.write("I deleted all the content of the file")

f2 = open("names.txt")
# print(f2.read())
f2.close()

## Two ways of creating a new file:
# 1) Opens a file for writing, but it doesn't exist > it creates it;
f3 = open("cities.txt", "w")
f3.close()

# 2) Creates the specified file, but returns an error if the exists;
if not os.path.exists("countries.txt"):
    f4 = open("countries.txt", "x")
    f4.close()
else:
    os.remove("countries.txt")