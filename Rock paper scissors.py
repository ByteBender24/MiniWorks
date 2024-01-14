print('''
Choose the mode of playing:
1 - Play against PC
2 - Two player mode''')

Mode=int(input("Enter the mode: "))

name1=input("Enter the name of Player 1: ")
if Mode==1:
    print ("     ", f"{name1} against PC")
else:
    name2=input("Enter the name of Player 2: ")

print ()
print('''
Pick the options from given below:
1 - Rock
2 - Scissors
3 - Paper
''')

print()
game_choice=1

score_p1=0
score_p2=0

while game_choice==1:
    import random   
    choice1=int(input(f"{name1}'s choice: "))
    if Mode==1:
        choice2 = random.choice([1,2,3]) 
        name2="PC"
        if choice2==1:
            print ("PC chose Rock")
        elif choice2==2:
            print ("PC chose Scissors")
        elif choice2==3:
            print ("PC chose Paper")
    elif Mode==2:
        choice2=int(input(f"{name2}'s choice: "))

    if choice1==1 and choice2==2:
        print ("\nRock wins over Scissors")
        print (f"{name1} wins")
        score_p1+=1
    elif choice1==1 and choice2==3:
        print ("\nPaper wins over Rock")
        print (f"{name2} wins")
        score_p2+=1
    elif choice1==2 and choice2==1:
        print ("\nRock wins over Scissors")
        print (f"{name2} wins")
        score_p2+=1
    elif choice1==2 and choice2==3:
        print ("\nScissors wins over Paper")
        print (f"{name1} wins")
        score_p1+=1
    elif choice1==3 and choice2==1:
        print ("\nPaper wins over Rock")
        print (f"{name1} wins")
        score_p1+=1
    elif choice1==3 and choice2==2:
        print ("\nScissors wins over Paper")
        print (f"{name2} wins")
        score_p2+=1
    elif (choice1==1 and choice2==1) or (choice1==2 and choice2==2) or (choice1==3 and choice2==3):
        print ("\nTie")
    elif ((choice1 not in [1,2,3]) or ((choice2 not in [1,2,3])) ):
        print ("\nReplay. You have mistyped. ")
    print ("- - - - - - - - - - - - - - - - - - - - - - - -")
    print ("\nDo you wanna play again?")
    print ("Choose 1 to continue")
    print ("Choose 2 to exit")

    game_choice = int(input("\n1 or 2 : "))
    print ()
    if game_choice == 2:
        print (f"{score_p1} games won by {name1}")
        print (f"{score_p2} games won by {name2}")
        print ("\nGAME EXIT!\nRun the program to play again\n")
        break
    if game_choice not in [1,2]:
        print ("Please enter a correct choice!")
        game_choice = int(input("\n1 or 2 : "))