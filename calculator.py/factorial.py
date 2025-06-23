def factorial(a):
    if a==1 or a==0:
        return 1
    else:
        return a*factorial(a-1)
print(factorial(10))
# here is the next method of same problem with the help of loop
c=10
fact=1
for i in range(c):
    fact=fact*(c-i)
print(fact)