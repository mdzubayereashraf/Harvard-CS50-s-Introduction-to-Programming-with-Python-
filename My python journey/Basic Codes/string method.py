#String Methods in Python
text = "Hello, World!"

#Using upper() method   
print(text.upper())

#Using lower() method
print(text.lower())

#Using title() method
print(text.title())

#Using strip() methodw
text_with_spaces = "   Hello, World!   "
print(text_with_spaces.strip())

#Using replace() method
print(text.replace("World", "Python"))

#Using split() method
print(text.split(","))

#Using join() method
words = ["Hello", "World"]
print(" ".join(words))

#Using find() method
print(text.find("World"))

#Using count() method
print(text.count("o"))

#Using startswith() method
print(text.startswith("Hello"))

#Using endswith() method
print(text.endswith("!"))
