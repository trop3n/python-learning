print("TEXT FORMATTER")
text = input("Enter the text you wish to format: ")
print(text)
answer = input("Select the formatting you want (1-4): 
 

if answer == "1":
    print(text.capitalize())
elif answer == "2":
    print(text.upper())
elif answer == "3":
    print(text.lower())
elif answer == "4":
    print(text.title())
else:
    print("Please select from the available options, 1 - 4.")