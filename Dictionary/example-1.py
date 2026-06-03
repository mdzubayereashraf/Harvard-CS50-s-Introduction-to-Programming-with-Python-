students = {
    "Harry": "Gryffindor",
    "Hermione": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student, students[student], sep=": ") #sep is used to specify the separator between the values. By default, it is a space, but we can change it to anything we want. In this case, we are using ": " as the separator between the student name and their house.
#when u only use print(student) it will only print the keys of the dictionary, but when u use print(student, students[student]) it will print both the keys and the values of the dictionary.