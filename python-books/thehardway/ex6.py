types_of_people = 10 # variable declaration, assigning number of people to an integer value of 10
x = f"There are {types_of_people} types of people." # variable declaration of x, using a and f-string to include the types_of_people variable into the string assignment

binary = "binary" # variable declaration
do_not = "don't" # variable declaration
y = f"Those who know {binary} and those who {do_not}." # variable declaration of y, including the two previous variables to form a string

print(x) # print statement printing the variable x
print(y) # print statement printing the variable y

print(f"I said: {x}") # print statement using f-strings to include to value of x in the string
print(f"I also said: '{y}'") # print statement using f-strings to include the value of y, but held in single quotes. The single quotes will be treated as part of the string.

hilarious = False # variable declaration to the boolean value of False
joke_evaluation = "Isn't that joke so funny?! {}" # variable declaration to a string value, which adds the False boolean from the previous variable declaration

print(joke_evaluation.format(hilarious)) # print statement that formats the joke_evaluation variable with the variable 'hilarious', which contains a string

w = "This is the left side of..." # variable declararion of a string
e = "a string with a right side." # another variable declaration of a string

print(w + e) # print statement that concatenates the two strings contained in the variables w and e