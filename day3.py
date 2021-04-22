print("#AGE CALCULATOR")
x=int(input("Enter the year you were born to calculate the age:"))
y=int(input("enter the current year:"))
age=int(y-x)
print("your age is:",age)

print("##############################################################")

print("#simple CALCULATOR")
a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
print("operations---")
print("1.add\n"\
      "2.subtract\n"\
      "3.multiplication\n"\
      "4.int division\n"\
      "5.floor division\n"\
      "6.modulus\n"\
      "7.power\n")
c=int(input("select operation")) 
if (c==1):
    print("your ans is:",a+b)
elif (c==2):
    print("your ans is",a-b)
elif (c==3):
    print("your ans is",a*b) 
elif (c==4):
    print("your ans is",a//b)
elif (c==5):
    print("your ans is",a/b)    
elif (c==6):
    print("your ans is",a%b)
else:
    print("your ans is",a**b)
    
print("######################################################################")  

print("#check the occurence of y in the string")
s="hello my name is yasmin"
print(s.count("y"))
print("#even indexing")
t=s[::2]
print(t)
