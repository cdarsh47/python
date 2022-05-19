# A program to add the MCQ questions and options in the database table
import pymysql.cursors

connection = pymysql.connect(host="localhost",user="root",password='',database='test')

db_object=connection.cursor()

check_tbl=db_object.execute("show tables like '%mcq%'")

def save_db(question,option1,option2,option3,option4,correct):
	query="INSERT INTO mcq (question,option1,option2,option3,option4,correct) VALUES ('"+question+"','"+option1+"','"+option2+"','"+option3+"','"+option4+"','"+correct+"')"
	status=db_object.execute(query)
	connection.commit()
	if status:
		print("Record added successfully")
		connection.close()	

def table_status():
	if check_tbl:
		Question=input("Please enter the MCQ question:")
		Option1=input("Please enter the first option:")
		Option2=input("Please enter the second option:")
		Option3=input("Please enter the third option:")
		Option4=input("Please enter the fourth option:")
		Correct=input("Please enter the correct option:")
		save_db(Question,Option1,Option2,Option3,Option4,Correct)

def main():
	table_status()

if __name__=='__main__':
	main()
