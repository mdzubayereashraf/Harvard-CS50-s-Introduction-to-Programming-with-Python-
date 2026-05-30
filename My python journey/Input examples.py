# Asking for user input
# name = input( "Enter your name :")
# name = name.strip() # I used this to skip white space
# name = name.title() # I used this method to capitilize of every word's fisrt character
# age = int(input( " Enter your age:"))
# mark = int(input("Enter your mark:"))


# #casual method of priting input function
# print("Your name is", name)
# print("Your age is", age)
# print("Your name is", mark)

# now I'm making codes more advanced and organised
name = input("Enter your name, please. ").strip().title() #name.capitalize() use only first  character of the string
age = int(input("Enter your age, please. "))
mark = int(input("Enter your mark, please. "))

# Using advanced print formula
print(f"Your name is : {name}")
print(f"Your age is : {age}")
print(f"Your mark is : {mark}")
print("Thank you for tunning us")