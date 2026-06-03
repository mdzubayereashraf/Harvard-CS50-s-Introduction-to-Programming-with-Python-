students = [
    {"name": "Harry", "house": "Gryffindor","patronus": "Stag"},
    {"name": "Hermione", "house": "Gryffindor","patronus": "Otter"},
    {"name": "Ron", "house": "Gryffindor","patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin","patronus": "Serpent"}
]
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", " )
    