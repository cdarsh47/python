import database,re

def contact_add():

	db,connection=database.main()

	check_tbl=db.execute("show tables like '%contact_book%'")

	if check_tbl:

		name = input("Please enter the full name:")

		cont_number = int(input("Please enter the contact number:"))

		email_id = input("Please enter the email address:")

		address = input("Please enter the address:")

		regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

		if name and cont_number and address and re.fullmatch(regex,email_id):

			Query='INSERT INTO contact_book(name,contact_number,email_id,address) values("'+name+'","'+str(cont_number)+'","'+str(email_id)+'","'+address+'")'
			status = db.execute(Query)
			connection.commit()
			
			if status:
				print("=========================")
				print("Record added successfully")
				print("=========================")
			else:
				print("There seems to be an issue!!")
			connection.close()	
			
		else:
			print("Please make sure you enter the proper values.")
			print("Email id should be in valid format.")

		main()

def contact_display():

	db,connection=database.main()

	db.execute("SELECT * FROM contact_book")
	
	contacts=db.fetchall()

	print("================================================================")
	print ("Here are all the contact book records.".center(60))
	print("================================================================")
	for contact in contacts:
		print(f" {contact['id']} , {contact['name']} , {contact['contact_number']} , {contact['email_id']} , {contact['address']}".center(20))

	connection.commit()	
	
	connection.close()
	
	print("================================================================")
	
	main()	

def contact_search():

	search_term=int(input("Please enter using which parameter you want to search the record? \n 1. press 1 for Name \n 2. press 2 for number \n 3. press 3 for email id \n 4. press 4 for address.:"))

	if search_term == 1:
		sql = """SELECT * FROM contact_book WHERE name LIKE %s"""
	elif search_term == 2:
		sql = """SELECT * FROM contact_book WHERE contact_number LIKE %s"""
	elif search_term == 3:
		sql = """SELECT * FROM contact_book WHERE email_id LIKE %s"""
	elif search_term == 4:
		sql = """SELECT * FROM contact_book WHERE address LIKE %s"""
	else:
		print("Invalid response given!!!")
	
	if sql:
		search_value=input("Please enter the search value:")		

		db,connection=database.main()

		db.execute(sql, (f'%{search_value}%'))

		contacts=db.fetchall()

		print("================================================================")
		print("Here are the found records.".center(60))

		if contacts:

			for contact in contacts:
				print("================================================================")
				print(f" {contact['id']} , {contact['name']} , {contact['contact_number']} , {contact['email_id']} , {contact['address']}".center(20))
				print("================================================================")
		
		connection.commit()
		
		connection.close()
		
		main()

def contact_delete():

	search_term=int(input("Please enter using which parameter you want to search the record? \n 1. press 1 for Name \n 2. press 2 for number \n 3. press 3 for email id \n 4. press 4 for address.:"))

	if search_term == 1:
		sql = """SELECT * FROM contact_book WHERE name = %s"""
		delete_sql = """DELETE FROM contact_book WHERE name = %s"""
	elif search_term == 2:
		sql = """SELECT * FROM contact_book WHERE contact_number = %s"""
		delete_sql = """DELETE FROM contact_book WHERE contact_number = %s"""
	elif search_term == 3:
		sql = """SELECT * FROM contact_book WHERE email_id = %s"""
		delete_sql = """DELETE FROM contact_book WHERE email_id = %s"""
	elif search_term == 4:
		sql = """SELECT * FROM contact_book WHERE address = %s"""
		delete_sql = """DELETE FROM contact_book WHERE address = %s"""
	else:
		print("Invalid response given!!!")

	if sql:
		search_value=input("Please enter the search value:")		
		print(search_value)
		db,connection=database.main()

		status= db.execute(sql, (search_value))

		print(status)

		contacts=db.fetchall()

		print("================================================================")
		print ("Here are the found records.".center(60))

		if contacts:

			for contact in contacts:
				print("================================================================")
				print(f" {contact['id']} , {contact['name']} , {contact['contact_number']} , {contact['email_id']} , {contact['address']}".center(20))
				print("================================================================")	

		affirm_resp=input("Are you sure you wish to delete this record?(y/n):")

		if affirm_resp == 'y':
			status = db.execute(delete_sql, (search_value))
			if status:
				print("=========================")
				print("Record deleted successfully")
				print("=========================")
			else:
				print("There seems to be an issue!!")
		
		connection.commit()		
		
		connection.close()
	
	main()	
					

def welcome():

	print("=====================================")

	print("Welcome to the contact book module!! ")
	
	print("=====================================")

def main():
	
	print("-------------------------------------------------")
	print("Please enter your choices from the below options.")
	print("-------------------------------------------------")
	print("Enter 1 to add the record in the contact directory.")
	print("-------------------------------------------------")
	print("Enter 2 to list all the record in the contact directory.")
	print("-------------------------------------------------")
	print("Enter 3 to search for a particular entry from the contact book.")
	print("-------------------------------------------------")
	print("Enter 4 to delete the record from the contact book.")
	print("-------------------------------------------------")
	print("Enter 5 to exit from the program.")
	print("-------------------------------------------------")
	response=int(input("Enter your choice:"))
	
	if response == 1:
		contact_add()
	elif response == 2:
		contact_display()
	elif response == 3:
		contact_search()
	elif response == 4:
		contact_delete()		
	elif response == 5:
		print("You are out of the contact book program!! Thank You.")		
	else:
		print("Nothing")	

if __name__=='__main__':
	welcome()
	main()