import math
def calculate_bmi(weight,height):
	final_value= (float(weight) / (float(height)/100)**2)
	print("your weight:",final_value)
	print('%.2f' %final_value)
	if(final_value <= 18.5):
		sentense="You are underweight."
	elif(final_value <= 24.9):
		sentense="You have a normal weight."
	elif(final_value <= 29.9):
		sentense="You are overweight"	
	elif(final_value <= 34.9):
		sentense="You are obese"
	else:
		sentense="You are severely obese."
	return sentense			

weight=input("Please enter your weight:")
height=input("Please enter your height in cm:")

if(weight and height):
	result=calculate_bmi(weight,height)
	print(result)
