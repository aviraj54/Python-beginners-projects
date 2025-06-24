target=9
array=[2,7,11,12]
dicto={}
for i,num in enumerate (array):
    complement=target-num
    if complement in dicto:
        print([dicto[complement],i]) 
    else:
        dicto[num]=i
                       
