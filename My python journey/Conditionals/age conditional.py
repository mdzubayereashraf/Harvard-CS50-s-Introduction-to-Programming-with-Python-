#Creating a age conditional statement
while True:
     age = int(input("Enter your age: "))

     if age < 0:
        print("Age cannot be negative. Please enter a valid age.")
     elif age > 120:
        print("Age cannot be greater than 120. Please enter a valid age.")     
     else:
        print("Your age is valid.")
        break

        
