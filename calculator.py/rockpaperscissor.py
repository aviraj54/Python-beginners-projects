import random

alternative = ['rock', 'paper', 'scissor']
co = 0
user = 0

for i in range(5):
    choice = input("""enter your choice:1.rock 2.paper 3.scissors""")
    computer_choice = alternative[random.randrange(0, 3)]
    
    if computer_choice == choice:
        print("both draw")
    elif choice == 'rock' and computer_choice == 'paper':
        print("you lost because comp choice=" + computer_choice)
        co += 1
    elif choice == 'rock' and computer_choice == 'scissor':
        print('you won because com choice=' + computer_choice)
        user += 1
    elif choice == 'paper' and computer_choice == 'rock':
        print("you won because comp choice=" + computer_choice)
        user += 1
    elif choice == 'paper' and computer_choice == 'scissor':
        print('you lose because com choice=' + computer_choice)
        co += 1
    elif choice == 'scissor' and computer_choice == 'paper':
        print("you won because comp choice=" + computer_choice)
        user += 1
    elif choice == 'scissor' and computer_choice == 'rock':
        print('you lose because com choice=' + computer_choice)
        co += 1
    else:
        print("invalid")

if co > user:
    print("you lost as whole ur =", user, "comp=", co)
elif user > co:
    print("you won your=", user, "comp=", co)
else:
    print("draw ur=", user, "comp=", co)
