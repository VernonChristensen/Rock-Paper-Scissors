# Vernon Christensen
# Rock Paper Scissors
#rps.py
# added comment for Github
import random
# Variables
pScore = 0
cScore = 0
ties = 0
cMoves = ["rock", "paper", "Scissors"]

# Welcome(Done)
#Print a welcome message
print("Welcometo rock, paper, Scissors")
# prompt for name
pName = input("what is your name?")


# Score Tracker
# Make a function
def printscore():
# Prints Score:
	print("score")
# Shows player score
	print(pName + ": " + str(pScore))
# Shows computer score
	print("computer Score: " + str(cScore))
# Shows how many toes
	print("Ties: " + str(ties))

# Game Loop
# loop until q is entered
while True:
	# Prompt for player mover (r, p, s,q)
	pMove = input("Enter 'r' for rock, 'p' for paper, 's' for Scissors or 'q' to quit")
# print the score
	printscore()
	if pMove == 'q': 
		break

# geta computer move (random)
	cMove = random.choice(CMoves)
# compare player move with the computer move
	# player picks rock
	if pMove == "r":
		print(pName + " picked Rock")
		if cMove == "rock":
			print("computer picks rock")
			print("Tie")
			ties += 1
		elif cMove == "paper":
			print("computer picks paper")
			print("paper covers Rock")
			cScore += 1 
		else:
			print("computer puck")
# player picks paper
	elif pMove == "p":
		pass
# player picks scissors
	elif pMove == "s":
		pass
# check if pMove is valid