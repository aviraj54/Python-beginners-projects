# this is a simple calculator project
a=input("a number")
b=input("another number")
a=int(a)
b=int(b)
choice=input(""" please enter your choice:
             1.addition
             2.subtraction
             3.multiplication
             4.division""")
choice=int(choice)
if choice==1:
    result=a+b
elif choice==2:
    result=a-b
elif choice==3:
    result=a*b
else:
    result=a/b
print("the require result is",result)