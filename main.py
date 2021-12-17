import random

choices = ["rock","paper","scissors"]

computer =random.choice(choices)
player = None

while player not in choices:
    player = input("rock,paper or scissors: ").lower()

print("computer:",computer)
print("player:",player)

if player == computer:
    print("successful")
else:
    print("wrong")