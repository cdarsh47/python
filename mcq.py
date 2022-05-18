# A Quiz program which asks questions with four answers and returns the Correct answers count at the end
mcq1={'question':'What is the capital of Japan?','option1':'Kyoto','option2':'Tokyo','option3':'Hiroshima','option4':'Nagasaki','correct':'Tokyo'}
mcq2={'question':'Which of these films are directed by Danny Boyle?','option1':'Trainspotting','option2':'Annihilation','option3':'Black Swan','option4':'Apocalypse now','correct':'Trainspotting'}
mcq3={'question':'Which of these books are written by Alex Garland?','option1':'Pines','option2':'Mystic River','option3':'Gone Girl','option4':'The Coma','correct':'The Coma'}
mcq4={'question':'Saskatoon is a city of which country?','option1':'USA','option2':'Canada','option3':'UK','option4':'France','correct':'Canada'}
mcq5={'question':'Which out of these is a PHP framework?','option1':'Django','option2':'Bootstrap','option3':'Wordpress','option4':'SASS','correct':'Wordpress'}

dictionary_set=[mcq1,mcq2,mcq3,mcq4,mcq5]
correct_answers=0

for incrementor_value,x in enumerate(dictionary_set,1):
	
	print("===============================")
	print(str(incrementor_value)+". "+x['question'])
	print("===============================")
	print('A:'+x['option1']+" || B:"+x['option2']+"\nC:"+x['option3']+" || D:"+x['option4'])
	print("--------------------------------")
	user_response=input('Please enter your right answer:')
	print("--------------------------------")
	if(user_response.lower()==x['correct'].lower()):
		print('Great!!! Right answer')
		correct_answers+=1
	else:
		print('Wrong Answer. Keep it going!!')

print("==========================")
if(correct_answers == len(dictionary_set)):
	print("Bravo!! You got all "+str(correct_answers)+" correct answers")
else:
	print("You got "+str(correct_answers)+" correct answers. Try to get all the answers right next time. Goodluck.")
print("==========================")