#asking user input
while True:
    n = int(input("Enter a number: "))
    if n < 0:
        continue #continue is used to skip the current iteration of the loop and move on to the next one. In this case, if the user enters a negative number, the loop will skip the rest of the code and prompt the user for input again.
    else:
        break #break is used to exit the loop entirely. In this case, if the user enters a non-negative number, the loop will break and the program will continue with the next lines of code after the loop.

for _ in range(n):
        print("Meow")       