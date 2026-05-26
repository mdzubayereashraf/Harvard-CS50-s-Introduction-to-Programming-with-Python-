#Creating a Hello function
#indent lines are part of the function.So, they will only run when the function is called.
#you don't have to use the same name for the parameter as the variable you pass in. 
#You can use any name you like for the parameter, as long as it is consistent within the function. 
#The parameter is just a placeholder for the value that will be passed in when the function is called.

def hello(to = "world"):
    print("Hello,",to) 

hello()
name = input("What's your name? ").strip().title()
hello(name)

#Creating a function to square a number
def main():
    x = int(input("Enter a number: "))
    print(f"The squre is : {square(x)}")

def square(n):
    return n ** 2

main()