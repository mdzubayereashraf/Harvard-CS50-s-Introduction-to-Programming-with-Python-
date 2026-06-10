for i in [0,1,2]:
    print("Meow")

for _ in range (5): #we use a variable right after for like i(i for integer), but we don't use it anywhere.Thats why is better to use underscore to define the varible.
    print("Meow") # here i didn't use loop variable so i named it (_)

for num in range(1,10):
    print(num) #here i used the loop variable

for character in "Python":
    print(character) #here i used the loop variable

for square in range(1,6):
    print(f"Square of {square} = {square**2}") 

for i in range (1,4):
    for j in range (1,4):
        print(f"i = {i}, j = {j}")
