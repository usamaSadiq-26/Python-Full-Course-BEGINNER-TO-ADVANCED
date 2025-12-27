#  print('hey this is \"100days python code\" challenge\nand i am usama, your python teacher')


# a = 2000
# b = "Ladin"
# c = False
# d = None
# a1 = 2


# print(a)
# print(b)
# print(c)
# print(d)
# print(a,b,c,d)
# print(a+a1)
# print(a-a1)
# print(a/a1)
# print(a*a1)
# print("The type of a is", type(a))
# print("The type of a is", type(b))
# print("The type of a is", type(c))
# print("The type of a is", type(d))


# #day06
# list1 = [1231,"LADIN",["WILL BE A PROFESSIONAL PYTHON DEVELOPER IN",2026]]
# print(list1)

# tuple1 = ((123,321),("LADIN",1232))
# print(tuple1)

# dict1 = {"Full name":"Usama Sadiq","Username":"LADIN","Age":25, "Sex":"Male", "Can Vote":True}
# print(dict1)


# #day07
# print(15+6) #Addition Operator
# print(15-6) #Subtraction Operator
# print(15*6) #Multiplication Operator
# print(15/6) #Division Operator
# print(15//6) #Modulus Operator
# print(5%3) #Floor Division Operator
# print(5**3) #Exponential Operator

# HOW TO MAKE A CALCULATOR BY USING PYTHON

# a = 5
# b = 3

# ans1 = a+b
# print("Addition of",a, "and",b,"is equals to", ans1)

# ans2 = a-b
# print("Subraction of",a, "and",b,"is equals to", ans2)

# ans3 = a*b
# print("Multiplication of",a, "and",b,"is equals to", ans3)

# ans4 = a/b
# print("Division of",a, "and",b,"is equals to", ans4)

# ans5 = a//b
# print("Modulus of",a, "and",b,"is equals to", ans5)

# ans6 = a%b
# print("Floor Division of",a, "and",b,"is equals to", ans6)

# ans7 = a**b
# print("Exponential poewr of",b, "on",a,"is equals to", ans7)


# day08
# calculator solution explained

# #day09
# def printyourname(): #function ka name printyourname
#     print("Hanzala1")
#     print("Hanzala2")
#     print("Hanzala3")
#     print("Hanzala4")




# def firstcall():
#     print("first function call")
#     return printyourname()


# firstcall()

# day10
# FUNCTION WITH ARGUMENTS AND PARAMETERS
# String Slicing, Operations in string:

# a = "Usama Sadiq"
# alen = len(a)

# print(alen)
# print(a[0:4])
# print(a[0:5])
# print(a[0:11])
# print(a[0:11])
# print(a[6:11])
# print(a[-6:11])
# print(a[-11:-6])

# for i in a:
#     print(i)


# DAY13

# STRINGS ARE IMMUTABLE IN PYTHON
# HOW TO FIND LENGTH OF A STRING IN PYTHON
# a = "hey this is usama and today i will tell you how we can change any str data into upper case and lower case"
# b = "today i wll go to work"

# print(len(a))
# print(len(b))

# HOW WE CAN CONVERT A STRING DATA INTO UPPER CASE AND LOWER CASE

# a = "upper"
# b = "LOWER"

# print(a.upper())
# print(b.lower())

# Day 13
# I will push the code soon
# HOW WE CAN REPLACE ANY WORD IN STR DATA AND WHAR RSTRIP METHOD DO?

# a = "Usama is a Web Developer!!!!!!!!"

# print(a.rstrip("!"))
# print(a.replace("Web","Python"))

# OTHER METHODS IN STR DATA TYPE

# a = "usama is a Web Developer!!!!!!!!"

# print(a.capitalize())           #first letter capital
# print(len(a))                   #length of str
# print(a.center(50))             #centered str with total width 50
# print(len(a.center(50)))        #length of centered str
# print(a.count("e"))             #count of e in str
# print(a.endswith("!!!!!!!"))    #check if str ends with given value
# print(a.endswith("!!!!@!!!!"))  #check if str ends with given value
# print(a.endswith("w", 5,12))    #check if str ends with given value in given range
# print(a.endswith("W", 5,12))    #check if str ends with given value in given range
# print(a.find("WebD"))           #find the index of first occurrence of given value

# a = "asdbaisfgauAo8e3028honx29h3d2xxn2h4b209u34n2"
# b = "USAMASADIQ"

# print(a.isalnum())  #check if all characters are alphanumeric
# print(b.isalnum())  #check if all characters are alphanumeric

# a = "alsdnu2n379absdADASd238he82"
# b = "ASssbaisadbubosnalAS"
# c = "asdasdalkbhakyvcqaoshdoao"

# # print(a.isalpha())
# # print(b.isalpha()) #check if all characters are alphabetic
# print(c.islower())
# print(a.islower())

# a= "Hello this is a variable for print method"
# b= "Hello this is a variable for \nprint method"

#print(a.isprintable())
#print(b.isprintable())


## today i am not feeling well, i will upload today's class. tomorrow.



#Conditional operators
# > , < , >= , <= , == , !=

# a = int(input("Enter your Marks in Python: "))

# if(a>=70):
#     print("According to your marks, your grade is: A ")

# elif(a>=50):
#     print("According to your marks, your grade is: B ")

# elif(a>=40):
#     print("According to your marks, your grade is: C ")

# else:
#     print("According to your marks, your grade is: F ")





# Nested Statement

a = int(input("Enter your Marks in Python: "))

if(a>=90):
    print("According to your marks, your grade is: A+ ")

elif(a>=40):
    if (a>=40 and a<50):
        print("According to your marks, your grade is: C ")
    elif(a>=50 and a<60):
        print("According to your marks, your grade is: C+ ")
    elif(a>=60 and a<70):
        print("According to your marks, your grade is: B ")
    elif(a>=70 and a<80):
        print("According to your marks, your grade is: B+ ")
    else:
        print("According to your marks, your grade is: A ")

else:
    print("According to your marks, your grade is: F ")