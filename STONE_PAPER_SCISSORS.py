import random

def print_score(u,c,d):
    print("You won %d games"%u);
    print("Computer won %d games"%c)
    print("%d games draw"%d)



options=['r','p','s']
totalgames=0
user_wins=0
computer_wins=0
draw=0

users_input=input()

while(users_input !='q'):
    computers_choice=random.choice(options)
    totalgames=totalgames+1


    if(users_input not in options):
        print("Retry")
        users_input=input()


    print("Computers choice",computers_choice)


    if(users_input=='r' and computers_choice=='p'):
        computer_wins=computer_wins+1
    elif(users_input=='s' and computers_choice=='p'):
        user_wins=user_wins+1
    elif(users_input=='p' and computers_choice=='r'):
        user_wins=user_wins+1
    elif(users_input=='p' and computers_choice=='s'):
        computer_wins=computer_wins+1
    elif(users_input=='r' and computers_choice=='s'):
        user_wins=user_wins+1
    elif(users_input=='s' and computers_choice=='r'):
        computer_wins=computer_wins+1
    else:
        draw=draw+1
    

    print_score(user_wins,computer_wins,draw)

    users_input=input()
    
if(user_wins>computer_wins):
    print("YOU WON!!")
elif(computer_wins>user_wins):
    print("YOU LOST!!")
else:
    print("DRAW")
        
    
