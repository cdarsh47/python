#the program for checking the password strength
import random
def password_checker():

	class check_strength:

		def __init__(self,pwd):
			print("in init")
			self.pwd=pwd

		def check_length(self):
			status=0
			if len(password_input) >= 12:
				status=1
			return status	

		def check_lower(self):
			status=0
			for char in self.pwd:
				if char.islower():
					status=1	
					break
			return status		
		
		def check_upper(self):
			status=0
			for char in self.pwd:
				if char.isupper():
					status=1	
					break
			return status

		def check_numeric(self):
			status=0
			for char in self.pwd:
				if char.isdigit():
					status=1
					break
			return status

		def check_specialchars(self):
			status=0
			special_list=['~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','/','.']
			special_exists=[char for char in self.pwd if char in special_list]
			if special_exists:
				status=1
			return status

	password_input=input("Enter the password that needs to be checked:")

	chk_pwd=check_strength(password_input)

	pwd_pros,pwd_cons=[],[]

	if chk_pwd.check_length():
		pwd_pros.append("Your password has 12 or more characters")
	else:
		pwd_cons.append("Your password have less than 12 characters")

	if chk_pwd.check_lower():
		pwd_pros.append("Your password has lowercase character")
	else:
		pwd_cons.append("Your password does not have lowercase character")

	if chk_pwd.check_upper():
		pwd_pros.append("Your password has uppercase character")
	else:
		pwd_cons.append("Your password does not have uppercase character")

	if chk_pwd.check_numeric():
		pwd_pros.append("Your password has a number")
	else:
		pwd_cons.append("Your password does not have a number")			
		
	if chk_pwd.check_specialchars():
		pwd_pros.append("Your password has a special character")
	else:
		pwd_cons.append("Your password does not have a special character")

	if pwd_pros:
		print("==========================")
		print("=====Password stregths====")
		print("==========================")
		for x,stmt in enumerate(pwd_pros,1):
			print(str(x)+":"+str(stmt))

	if pwd_cons:
		print("==========================")
		print("=====Password weaknesses====")
		print("==========================")
		for x,stmt in enumerate(pwd_cons,1):
			print(str(x)+":"+str(stmt))

def password_generator():
	numbers=['0','1','2','3','4','5','6','7','8','9']
	lower_alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	upper_alphabets=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	special_list=['~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','/','.']
	password_list=[]

	password_list=random.sample(lower_alphabets, 4)+random.sample(upper_alphabets, 4)+random.sample(numbers, 2)+random.sample(special_list, 2)
	random.shuffle(password_list)
	password_string = ''.join(map(str, password_list))
	return password_string
	
print("========================================")
print("PASSWORD CHECKER/GENERATOR")
print("========================================")
print("Type 1 for Password Checking")
print("Type 2 for Password Generator")
print("========================================")
response=input("Please enter your input:")
print('========================')
if response=='1':
	result=password_checker()
elif response=='2':	
	result=password_generator()
	print("Your new generated password is:",result)	
else:
	print("Either it is bad value enetered or the value does not fall in above mention range.")		