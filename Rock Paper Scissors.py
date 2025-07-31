
import random

print("===================")
print("Rock Paper Scissors")
print("===================")

print("1) ✊")
print("2) ✋") 
print("3) ✌️")

player = int(input("Pick a number: "))
cpu = random.randint(1,3)

if player==1:
    print("You chose: ✊")
elif player==2:
    print("You chose: ✋")
elif player==3:
    print("You chose: ✌️")
else:
    print("Please pick a number 1-3.")

if cpu==1:
    print("CPU chose: ✊")
elif cpu==2:
    print("CPU chose: ✋")
elif cpu==3:
    print("CPU chose: ✌️")
else:
    print("Please pick a number 1-3.")

if player==1 and cpu==3:
    print("Rock beats Scissors so PLAYER wins!")
elif player==3 and cpu==1:
    print("Rock beats Scissors so CPU wins!")
elif player==3 and cpu==2:
    print("Scissors beats Paper so PLAYER wins!")
elif player==2 and cpu==3:
    print("Scissors beats Paper so CPU wins!")
elif player==2 and cpu==1:
    print("Paper beats Rock so PLAYER wins!")
elif player==1 and cpu==2:
    print("Paper beats Rock so CPU wins!")
elif player==2 and cpu==2:
    print("TIE")
elif player==1 and cpu==1:
    print("TIE")
elif player==3 and cpu==3:
    print("TIE")
else:
    print("Try again.")


