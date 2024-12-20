# imports the argv method from the sys library
from sys import argv

# specifies the parameters for argv
script, filename = argv

# txt variable, opens the filename specified in the argv input
txt = open(filename)

# print message with f string, print the contents of the file to the console
print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

# prints a message, with a prompt to use the input response as a new variable
print("Type the filename again:")
file_again = input("> ")

# repeats the process again using user input instead of the argv method
txt_again = open(file_again)

# print the contents of the variable, which is a file, by reading and 
# printing to the console
print(txt_again.read())
txt_again.close()