# Calculating length of a string
Name = "zubayer"
print(len(Name))

#Concatenation of strings
str1 = "Muhammad"
str2 = "Zubayer"
merge_string1 = str1 + str2
print(merge_string1)
merge_string2 = str1 +' '+ str2 # you needda give a space between ' and '
print(merge_string2)

# spiting line in string
paragraph1 = "This an example of a string.\nCan't you see it?"
print(paragraph1)

#creating a tab space in string
paragraph2 ="hey bro what's up? \thow's going?"
print(paragraph2)

#String methods
print(Name.upper()) #upper case
print(Name.lower()) #lower case
print(Name.title()) #title 

#Concatenation of string with f'   '
New_way = f'{str1} E {str2}' # this is also a way to concatenate string with space between them.
print(New_way) 