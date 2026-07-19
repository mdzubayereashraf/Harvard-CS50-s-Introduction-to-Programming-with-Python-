# Creating a student details class along with objects

class Student:
    def __init__(self, name , mark , attendance): #here self is object variable and others are class variables. 
        self.name = name
        self.mark = mark
        self.attendance = attendance
        
    def calculate_grade(self):
        if self.mark >= 90:
            return "A+"
        elif self.mark >= 80:
            return "A"
        elif self.mark >= 70:
            return "A-"
        elif self.mark >= 60:
            return "B"
        else:
            return "failed"
        
        

myself = Student("Zubayer", 80, 90) # creating object using the class(blue print) # here i used the class (Student) to make real objects.
 
print(myself.calculate_grade()) #here myself is a object and show is class function which is called method.Any functions created in class are called methods.


        