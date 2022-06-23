import re

def main():

	print("------------------------------------")
	print("Welcome to the email slicer program.")
	print("------------------------------------")

	email_id=input("Please enter your email id:")

	regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

	if re.fullmatch(regex,email_id):

		sliced=email_id.split('@')

		print(sliced[0],sliced[1])

		print("================================")
		print("The username is :",sliced[0])
		print("================================")
		print("The domain name is :",sliced[1])
		print("================================")

	else:
		print("Please enter a valid email")

if __name__ == '__main__':
	main()		