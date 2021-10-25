from sys import argv

script, file = argv
file_open = open(file)
print(file_open.read())

file_again = input()
file_again_open = open(file_again)
print(file_again_open.read())
