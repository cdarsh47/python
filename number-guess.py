import random

class number_guess:

	def __init__(self):
		self._random_number=self.generate_number()
		self._predict_count=0
		self._predict_number=0

	@staticmethod
	def generate_number():
		random_number=random.randrange(1, 50)
		return random_number

	@property
	def get_number(self):
		return self._random_number

	@property	
	def predict_count(self):
		return self._predict_count	

	def show(self):
		print("===============================================================================")
		print("================= WELCOME TO THE GUESS THE NUMBER GAME ========================")
		print("The number that you will have to guess will be in the range of 1-50.")
		print("We will generate the number and you will be asked to enter the number to guess.")
		print("============================== ALL THE BEST ===================================")
		print("===============================================================================")

	def process_game(self):
		self.prompt_user()
		self.guess_number()

	def prompt_user(self):
		input_number=int(input("Please enter the number:"))
		self._predict_number=input_number
		self._predict_count += 1

	def guess_number(self):
		msg,success='',0

		if self._predict_number == self._random_number:
			msg += '============================================'
			msg += '\nWoohoo You have guessed the number right!!!!'
			msg += '\n============================================'
			success=1

		if self._predict_number < self._random_number:
			msg += "Wrong number guessed."
			msg += "\nYour guessed number is less than the generated number."

		if self._predict_number > self._random_number:
			msg += "Wrong number guessed."
			msg += "\nYour guessed number is greater than the generated number."	

		if abs(self._predict_number - self._random_number) <= 5 and success==0:
			msg += "\nHINT: You are very close. The difference between the numbers are less than 5. Go Again!!"

		if success == 0:

			if self._predict_count in (10,20,30,40,50):
				resp= input("Wanna give up?(y/n)")
				if resp == 'y':
					print("Number of times you attempted:",self._predict_count)
					print("The generated number was:",self._random_number)
					return False		

			print("Number of times you attempted:",self._predict_count)
			print(msg)
			self.process_game()
		else:
			print("Number of times you attempted:",self._predict_count)
			print(msg)		

def main():
	number_ob=number_guess()
	number_ob.show()
	result=number_ob.process_game()


if __name__ == '__main__':
	main()
