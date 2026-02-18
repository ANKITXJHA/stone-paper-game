# rock paper siscor  game
print("WELCOME TO ROCK PAPER SCISSOR GAME")
print("Enter the only  first letter in lowercase")
youstr= input("enter your choice : ")
import random
computer= random.choice([1,2,3]) 
youdict={"r":1,"p":2,"s":3} 
yourev={1:"rock🪨",2:"Paper📰",3:"scissors✂"}
you =youdict[youstr]
if(you == computer):
    print(f"you choose:{yourev[you]}\ncomputer choose:{yourev[computer]}")
    print("Game Draw")

else:
    if(computer ==1 and you==2):
        print(f"you choose:{yourev[you]}\ncomputer choose:{yourev[computer]}")
        print("You win!")

    elif(computer ==1 and you ==3):
        print(f"you choose:{yourev[you]}\ncomputer choose:{yourev[computer]}")
        print("computer win!")

    if(computer ==2 and you ==1):
        print(f"you choose:{yourev[you]}\ncomputer choose:{yourev[computer]}")
        print("computer  win!")

    if(computer ==2 and you ==3):
        print(f"you choose:{yourev[you]}\ncomputer choose:{yourev[computer]}")
        print("You win!")


    if(computer ==3 and you ==1):
        print(f"you choose:{yourev[you]}\ncomputer choose:{yourev[computer]}")
        print("You win!")
    if(computer ==3 and you ==2):
        print(f"you choose:{yourev[you]}\ncomputer choose:{yourev[computer]}")
        print("computer win!")
    
    

     


