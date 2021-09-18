rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print(rock,paper,scissors,sep="  ")


print("WELCOME")
print("GET READY TO PLAY THIS GAME")
print("THE ONE WHO WILL SCORE 5 points FIRST IS THE WINNER ")
print("MEANS-:")

print("if you scores 5 point first then you will win")
print("if computer scores 5 points first then he will win")

start=input("press enter to start this game-:")



print("")
print("")
print("")
print("")
print("")


import random
import time
game=[rock,paper,scissors]

user_win=0
comp_win=0
round=1
while user_win<5 and comp_win<5:
 user_win=user_win
 comp_win=comp_win
 print("ROUND ",round)
 round=round+1
 print('''Type
 0 for ROCK
 1 for PAPER
 2 for SCISSORS''')
 user=int(input("what do you choose?"))

 if user>=0 and user<3:
  print("")
  print("you choose",game[user])
  print("")
  print("Computer is choosing.....")
  time.sleep(1)
  print("")
  print("Computer chooses:")

  random_number=random.randint(0,2)
  comp_move=game[random_number]
  print(comp_move)

  if user==0:
    if random_number==1:
        comp_win = comp_win + 1
        print("you lose,computer gets 1 point")


    elif random_number==2:
        user_win = user_win + 1
        print("you won,you got 1 point")


    else:
        print("ohh! it's a tie")

  elif user==1:
    if random_number==2:
        print("you lose,computer gets 1 point")
        comp_win = comp_win + 1
    elif random_number==0:
        print("you won,you got 1 point")
        user_win = user_win + 1
    else:
        print("ohh! it's a tie")

  elif user==2:
    if random_number==0:
        print("you lose,computer gets 1 point")
        comp_win = comp_win + 1
    elif random_number==1:
        print("you won,you got 1 point")
        user_win = user_win + 1
    else:
        print("ohh! it's a tie")

  print("")
  print("")
  print("")
  print("")
  print("scorecard-:")
  print("your score=",user_win)
  print("computer score=",comp_win)
 else:
    print("wrong option selected")
 time.sleep(2)

 print("")
 print("")
 print("")
 print("-------------------------------------------------------------------------------------------------------------------------")
 print("")
 print("")
 print("")


if user_win==5:
    print("congratulations you win")
if comp_win==5:
    print("""oh! no, you lost
    better luck next time""")








