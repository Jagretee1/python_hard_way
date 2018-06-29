from sys import argv

script, filename = argv

print("We are going to erase %r." % filename)
print("If you do not want that, hit CTRL-C .")
print("If you do want that hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Trunicating the file. Goodbye!")
target.truncate()

print("Now I am goint to ask you for three lines.")

Line1 = input("line 1:")
Line2 = input("line 2:")
Line3 = input("line 3:")

print("I'm going to write these to the file.")

target.write(Line1)
target.write("\n")
target.write(Line2)
target.write("\n")
target.write(Line3)
target.write("\n")

print("And finally we close it.")
target.close()
