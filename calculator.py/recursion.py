## fomdomg fabonachi series  using recursion
n=int(input('how many n numbers do u want fabonachi series'))
def fab(n):
    if n==1 :
        return 1
    elif n==2:
        return 1
    else:
        return fab(n-1) + fab(n-2)
print(fab(n))