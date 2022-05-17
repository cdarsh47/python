#This is a program for madlib where after taking the values the text is displayed with the user input value placed in it
import random
def generatemadlib(generated_number,response_one,response_two):
	
	""" 
	This function takes the input responses from the user and generate a sentence

	"""
	temp1="{input1} as a professional thief who steals information by infiltrating the{input2} of his targets."
	temp2="{input1} is a robber who is trying to commit a big heist in{input2}."
	temp3="{input1} is searching for the men who stole her/his{input2} and which was a last gift given to her/him "
	temp_disc={1:temp1,2:temp2,3:temp3}	

	line=temp_disc[generated_number].format(input1=response_one,input2=response_two)
	return line

def main():
	""" 
	This is the main function in the program 
	
	"""
	generated_number=random.randrange(1,4)

	if(generated_number==1):
		response_one=input("what is your name?:")
		response_two=input("what would you like to infiltrate?:")

	elif(generated_number==2):
		response_one=input("what is your name?:")
		response_two=input("Where would you like to go?:")
	else:
		response_one=input("What is your name?:")
		response_two=input("What has been stolen from you?:")
	
	result=generatemadlib(generated_number,response_one,response_two)
	print(result)

#print(__name__)
main()


