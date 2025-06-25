number=int(input("enter any digit number whose reverse is to be printed."))
reverse=0
while(number!=0):
    remainder=number%10
    reverse=reverse*10+remainder
    number=int(number/10)
print("the number in reverse order:",reverse)