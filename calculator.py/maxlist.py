list1=[1,2,3,4,5,6,7,8,9,10]
max=list1[0]
min=list1[0]
for i in range(len(list1)):
    if max<list1[i]:
        max=list1[i]
    if min>list1[i]:
        min=list1[i]
print(f"the maximum value is{max} and minimum is {min}in the list.")