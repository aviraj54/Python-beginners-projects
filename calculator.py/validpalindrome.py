# to find wheteher the given value is palindrome or not by removing all the extra signs and symbols rather than alphabets
value=input("enter any string value")
length=len(value)
length-=1
reverse=""
nvalue=""
value=value.lower()
while(length!=-1):
    if ord(value[length])>=97 and ord(value[length])<=122:
        reverse=reverse+value[length]
        length -=1
    else:
        length-=1
        continue
for i in range(len(value)):
    if ord(value[i])>=97 and ord(value[i])<=122:
        nvalue+=value[i]
if (reverse==nvalue):
    print("palindrome")
else:
    print("not palindrome")