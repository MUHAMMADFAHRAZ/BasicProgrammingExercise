#program created by muhamad fahraz firdaus
#ti22i class

#input data


import array
from operator import truediv


print("hello this is biodata app ") 
name = input("please, enter your name! ")
age = int (input("enter your age! "))
kls = input("enter your class!  ")
major = input("enter your major!  ")
hobby1 = (input("what is your first hobby?  "))
hobbiy2 = (input("what is your second hobby?  "))
hobby3 = (input("what is your third hobby?  "))
hobbies = [hobby1,hobbiy2,hobby3]
baso = bool (input("do you like baso? y for yes, blank for no "))
motto = input("enter your life motivation! ")

#display
print("My biodata")
print("Name : ",name)
print("age : ",age)
print("class : ",kls)
print("major : ", major)
print("hobbies : ", hobbies)
print("like baso : ", baso)
print("motto : ", motto)
print("name type is:", type(name))
print('age type is :', type(age))
print("class type is :", type(kls))
print("major type is :", type(major))
print("hobbies type is :", type(hobbies))
print("baso type is :", type(baso))
print("motto type is :", type(motto))