#Python program to play the game Rock, Paper, Scissors
import random

game_list=['rock','paper','scissors']


def main():

	print("Let's Start the game")

	cpu_choice=random.choice(game_list)

	response=input('Enter the choice: ')

	check_winner(response,cpu_choice)

def check_winner(user1,user2):
	user1=user1.lower()
	again=False

	print("Your Entered value: "+user1)
	print("Computer chosen value: "+user2)

	if(user1 not in ['rock','paper','scissors']):
		print("Wrong value entered")
		again=True
	elif(user1==user2):
		print("The Game Draws")
		again=True
	elif((user1=='rock' and user2=='paper') or (user1=='paper' and user2=='rock')):
		print("The Paper wins")
	elif((user1=='scissors' and user2=='paper') or (user2=='scissors' and user1=='paper')):
		print("The Scissors wins")
	elif((user1=='rock' and user2=='scissors') or (user1=='scissors' and user2=='rock')):
		print("The Rock wins")	
	else:	
		print("some other issues")

	if again:
		main()	

main()
