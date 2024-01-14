import random
x=random.choice(["KRATOS","LEONIDAS","MARIO","MAGNETO","WOLVERINE","MATRIX","TERMINATOR"])
for i in range(len(x)):
    print ("_",end=" ")

inputs = []
corrects = []

if len(x)<10:
    lives = random.randrange(5,7)
    life = lives
    n=random.randint(2,3)
else:
    lives = random.randrange(11,14)
    life = lives
    n=random.randint(6,8)

print(f"You have {lives} lives.")

while True:
    ch=input("\nEnter a character: ")[0]
    ch=ch.upper()
    if ch in inputs:
        print("Already entered!")
        continue
    inputs.append(ch)
    if ch in x:
        corrects.append(ch)
    for elt in x:
        if elt == ch or elt in corrects:
            print(elt, end = " ")
        else:
            print("_", end = " ")
    print()
    if ch not in x :
        print(f"You entered wrong character.     LIVES = {lives-1}")
        lives = lives - 1
        
    if len(set(corrects)) == len(set(x)):
        print("\nYOU WON!\n")
        print()
        break
    if lives == 0:
        print (f"The correct word was {x}")
        print("\nYOU LOSE. PLEASE TRY AGAIN.\n")
        break
    if lives<life-n:
        if x=="KRATOS":
            y=random.choice(["God killer","Ghost of Sparta","God of war"])
            print(f"\n                                 CLUE : {y}")
        elif x=="LEONIDAS":
            y=random.choice(["300","This is Sparta!"])
            print(f"\n                                 CLUE : {y}")
        elif x=="MARIO":
            y=random.choice(["It's a me","Italian Plumber","Nintendo"])
            print(f"\n                                 CLUE : {y}")
        elif x=="MAGNETO":
            y=random.choice(["Metal Manipulation","X-men"])
            print(f"\n                                 CLUE : {y}")
        elif x=="WOLVERINE":
            y=random.choice(["X-men","Adamantium","Regeneration"])
            print(f"\n                                 CLUE : {y}") 
        elif x=="MATRIX":
            y=random.choice(["Keanu Reeves","Red pill,Blue pill"])
            print(f"\n                                 CLUE : {y}")
        elif x=="TERMINATOR":
            y=random.choice(["Arnold","John Connor","Hasta la vista Baby"])
            print(f"\n                                 CLUE : {y}") 