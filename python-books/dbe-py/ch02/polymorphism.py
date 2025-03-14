def example():
    print("in example")

example()

alias = example
alias()

# the function "example()" is renamed to "alias()" by setting it to the value of the alias variable.
# alias() can be called and the logic of the example() function will be used, since the connection is
# maintained to the original code in the example() function.