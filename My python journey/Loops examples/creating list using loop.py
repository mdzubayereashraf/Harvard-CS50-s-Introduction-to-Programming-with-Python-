#Creating list using for loops
lst = [x for x in range(10)]
print(lst)

squares = [x**2 for x in range(10)]
print(squares)

cubes = [x**3 for x in range(10)]
print(cubes)

even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)

odd_numbers = [x for x in range(20) if x % 2 != 0]
print(odd_numbers)

