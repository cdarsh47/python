#program using files function
import os
import sys

encod=sys.getdefaultencoding()

def get_response_mode():
	print("======================================")
	print("Please select which activities you want to do with files")
	print("======================================")
	print("1. Create a file.")
	print("2. write in a file")
	print("3. Read a file")
	print("4. Delete a file.")
	print("5. Exit from the program.")
	print("======================================")
	return int(input("Enter the choice in numbers:"))

def process_response(response):
	if response==1:
		file_response=input("Enter the filename:")
		if os.path.isfile(file_response):
			print("|||||||||||||||||||||||||||")
			print("|||||||File exists|||||||||")
			print("|||||||||||||||||||||||||||")
		else:
			f=open(file_response,mode='x')
			f.close()
			if(os.path.isfile(file_response)):
				print("|||||||||||||||||||||||||||")
				print("|||||||File Created|||||||||")
				print("|||||||||||||||||||||||||||")
		main()		
	elif response==2:
		file_response=input("Enter the filename:")
		text_reponse=input("Enter the content you want to write:")
		if text_reponse:
			f=open(file_response,mode="at")
			text_reponse += "\n"
			f.write(text_reponse)
			f.close()
		print("||||||||||||||||||||||||||||||||||||||")
		print("|||Done!! the file has beeen saved.|||")
		print("||||||||||||||||||||||||||||||||||||||")	
		main()
	elif response==3:
		file_response=input("Enter the filename:")
		print("---------------------------------")
		with open(file_response,'r') as f:
			for line in f:
				print(line)
		print("---------------------------------")		
		f=open(file_response,mode="rt",encoding=encod)
		#print("---------------------------------")
		#print(f.read())
		#print("---------------------------------")
		write_response=input("Do you wish to update the file(y/n)?:")
		if write_response.lower()=='y':
			append_response=input("Enter your text to update in file:")
			if append_response:
				g=open(file_response,mode="at",encoding=encod)
				append_response += "\n"
				g.write(append_response)
				g.close()
				print("||||||||||||||||||||||||||||||||||||||")
				print("|||Done!! the file has beeen saved.|||")
				print("||||||||||||||||||||||||||||||||||||||")
		f.close()
		main()
	elif response==4:
		delete_response=input("Enter the filename to delete:")
		if delete_response and os.path.isfile(delete_response):
			os.remove(delete_response)
			print("||||||||||||||||||||||||||||||||||||||")
			print("The file has been deleted!!!")
			print("||||||||||||||||||||||||||||||||||||||")
		else:
			print("||||||||||||||||||||||||||||||||||||||")
			print("The file does not exists.")
			print("||||||||||||||||||||||||||||||||||||||")	
		main()		
	elif response==5:
		print("||||||||||||||||||||||||||||||||||||||")
		print("You are out of the program now!!")
		print("||||||||||||||||||||||||||||||||||||||")	
	else:
		print("||||||||||||||||||||||||||||||||||||||")
		print("Please enter valid choice(1-5).")
		print("||||||||||||||||||||||||||||||||||||||")

def main():
	response=get_response_mode()
	process_response(response)	

if __name__ == '__main__':
	main()