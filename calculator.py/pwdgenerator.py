# this is strong password generator program
import random
spchar="!@#$%^&*()_{}:><,.?`~"
num="1234567890"
lcase="abcdefghijklmnopqrstuvwxyz"
ucase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i  in range(8):
    sc=spchar[random.randrange(0,len(spchar))]
    n=num[random.randrange(0,len(num))]
    n2=num[random.randrange(0,len(num))]
    lc=lcase[random.randrange(0,26)]
    n3=num[random.randrange(0,len(num))]
    lc3=lcase[random.randrange(0,26)]
    lc2=lcase[random.randrange(0,26)]
    uc=ucase[random.randrange(0,26)]
    pwd=lc+lc2+lc3+uc+n+sc+n3+n2
print("the generated password is:",pwd,len(pwd))