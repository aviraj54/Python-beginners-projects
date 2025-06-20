import random
options=['apple','ball','cat','dog']
choice=options[random.randrange(0,4)]
total_score=len(choice)
run=False
guessed=("")
score=0
for i in range(len(choice)):
    guess=("")
    guess=input("enter your guess")
    if guess in choice:
        score+=1
        guessed+=guess
        for x in choice:
            if x in guessed:
                print(x)
            else:
                print("__")
    else:
        for i in choice:
            print("__")
if score==total_score:
    print("you won")
else:
    print("you losose")