# A Quiz program which fetches the questions with four options from the Database table and returns the Correct answers count at the end
import pymysql.cursors

connection = pymysql.connect(host="localhost",user="root",password='',database='test')

db_object=connection.cursor()

check_tbl=db_object.execute("show tables like '%mcq%'")

def get_count():
	db_object.execute("select count(id) from mcq")
	result=db_object.fetchone()
	return result[0]

if check_tbl:
	correct_answers=0
	db_object.execute("SELECT * FROM mcq")
	output=db_object.fetchall()
	mcq_count=get_count()
	for incrementor_value,x in enumerate(output,1):
		question,option1,option2=str(x[1]),str(x[2]),str(x[3])
		option3,option4,correct=str(x[4]),str(x[5]),str(x[6])

		print("===============================")
		print(str(incrementor_value)+". "+question)
		print("===============================")
		print('A:'+option1+" || B:"+option2+"\nC:"+option3+" || D:"+option4)
		print("--------------------------------")

		user_response=input('Please enter your right answer:')
		print("--------------------------------")
		if(user_response.lower()==correct.lower()):
			print('Great!!! Right answer')
			correct_answers+=1
		else:
			print('Wrong Answer. Keep it going!!')
	print("==========================")
	if(correct_answers == mcq_count):
		print("Bravo!! You got all "+str(correct_answers)+" correct answers")
	else:
		print("You got "+str(correct_answers)+" correct answers. Try to get all the answers right next time. Goodluck.")
	print("==========================")