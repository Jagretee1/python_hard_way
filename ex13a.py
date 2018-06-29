from sys import argv

script, first, second, third = argv

print("What do you want the script to be called?"),
script = input()
print("What do you want your first argument?"),
first = input()
print("What do you want your second argument to be?"),
second = input()
print("What do you want to be your third argument?"),
third = input()
print(" Your script name is: {}, your first argument name is: {}, second is: {}, third is: {}".format(script, first, second, third))
print("{}{}{}{}".format(script, first, second, third))
