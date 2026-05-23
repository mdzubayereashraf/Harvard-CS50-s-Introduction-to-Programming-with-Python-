#Creating a list of string
names = ["zubayer", "sabbir", "sajid", "sharif"]
print(names)

#Accessing string from list
print(names[0]) #first element of the list
print(names[1]) #second element of the list
print(names[2]) #third element of the list
print(names[3]) #fourth element of the list

#Accessing string from list with negative index
print(names[-1]) #last element of the list
print(names[-2]) #second last element of the list
print(names[-3]) #third last element of the list    
print(names[-4]) #fourth last element of the list

#Accessing string from list with slicing list_name[start:stop]
print(names[0:2]) #first two elements of the list
print(names[1:3]) #second and third elements of the list
print(names[2:4]) #third and fourth elements of the list 

#Accessing string from list with slicing list_name[start:stop:step]   
print(names[:3]) #first three elements of the list
print(names[1:]) #second to last elements of the list

#Adding elements in list in the last position 
names.append('Khalek_kaku')
print(names)

#Adding elements in list in the first position
names.insert(0,'Sajedul')
print(names)

#Adding elements in list in any positions
names.insert(3,'Kawser')
print(names)