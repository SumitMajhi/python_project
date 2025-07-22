print("🎮 Welcome to My Game and test your luck ! Good luck 🤞")
print(f" select '1' for Stone \n select '2' for Paper \n select '3' for Scissor \n select '4' to exit")
import random
def check(user, comp):
    if (comp==user):
        return 0
    if(comp==1 and user==3) or (comp==2 and user==1) or (comp==3 and user==2):
        return 1
    else:
        return 2

weapons = {1:"Stone ✊", 2:"Paper 🖐️", 3:"Scissor ✌️", 4:"Exit"}

while True:
    try:
        user = int(input("Your weapon:"))
    except ValueError:
        print("Please enter a valid number (1-4)")
        continue

    if user == 4:
        print("Thanks for playing 💖")
        break

    if user not in [1,2,3]:
        print("invalid option, Please enter between 1-3 only.")
        continue
    
    comp=random.randint(1,3)
    print(f" Your weapon {weapons[user]} \n computer's weapon {weapons[comp]}")

    score=check(user,comp)
    if (score==0):
        print("Draw 🤝")
    elif (score==1):
        print("You Won🏆😄")
    else:
        print("you lose 👎😞")