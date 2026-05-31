#Match-Case functions
name = input("Enter the name of the character: ")
# match name :
#     case "Harry":
#         print("Gryffindor")
#     case "Hermione":
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffindor")
#     case _:
#         print("Who?")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case _:
        print("Who?")   
