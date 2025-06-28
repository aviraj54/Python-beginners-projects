# to print fabonachi series up to desired number of times
a=1
b=1
c=1
dtime=int(input("enter the desired numbers of fabonacchi series u wanna print"))
for i in range(dtime):
    if i ==0:
        print(i+1)
    elif i==1:
        print(i)
    else:
        c=a+b
        print(c)
        a=b
        b=c