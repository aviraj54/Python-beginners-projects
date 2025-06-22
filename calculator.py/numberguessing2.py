import random
number=random.randrange(0,100)
stop=True
while  stop:
    a=0
    b=0
    ans=input("enter your guessed number:")
    ans=int(ans)
    a=number-number%10
    b=number+10-number%10
    if (ans != number):
        print("number is between",a,"annd",b)
    else:
        stop=False
print("game is finished u r right")