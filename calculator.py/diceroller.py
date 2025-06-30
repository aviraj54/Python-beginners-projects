#simple dice rolling game to meet up the desired target
import random
print("""this is a simple die rolling game in which you have to 
      choose the targeted number to reach and number of times you want to roll the die 
      the targeted number should be achieved with in the number of time and you will win.""")
target=int(input('enter the target you want to achieve and remember the dice only contains 0 to 6 numbers.'))
i=0
req=0
ntimes=int(input("enter the number of times you wanna scroll the dice."))
for i in range(ntimes):
    print('this is your',i,'roll')
    roll=input('press a to roll the dice.')
    if roll=='a':
        n=random.randrange(0,7)
        print('you got',n,'in this roll')
        req+=n
    if req>=target:
        print("you achieved it")
        break
    ntimes-=1
if req==target:
    print('you got the target.')
else:
    print('so sad! you failed.')