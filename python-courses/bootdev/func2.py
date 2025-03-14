def create_introduction(name, age, height, weight):
    first_part = "Your name is " + name + " and you are " + age + " years old."
    second_part = "You are " + height + " meters tall and weigh " + weight + " kilograms."
    full_intro = first_part + " " + second_part
    return full_intro

my_name = "Jason"
my_age = "33"

intro = create_introduction(my_name, my_age, "1.8", "80")
print(intro)