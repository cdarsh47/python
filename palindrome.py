import time

def calculate_time(func):
	def wrapper(*args,**kwargs):
		start=time.time()
		result=func(*args,**kwargs)
		end=time.time()
		print("Time taken for this method to complete is:"+str((end-start)*1000)+" mil sec \n")
		return result
	return wrapper

@calculate_time	
def method1(response):
	
	print("========== using method2 ============")	
	
	response_string = response.replace(' ', '').lower()
	
	copy_string=response_string[::-1]

	if response_string == copy_string:
		print('----------------------------------')
		print("The entered string is palindrome.")
		print('----------------------------------')
	else:
		print('----------------------------------')
		print("The entered string is not palindrome.")
		print('----------------------------------')	

@calculate_time
def method2(response):
	
	print("========== using method2 ============")
	
	response_string = response.replace(' ', '').lower()

	length_counter=len(response_string)-1
	
	reverse_string=''
	
	while length_counter != -1:
		reverse_string += response_string[length_counter]
		length_counter -= 1

	if response_string == reverse_string:
		print('----------------------------------')
		print("The entered string is palindrome.")
		print('----------------------------------')
	else:
		print('----------------------------------')
		print("The entered string is not palindrome.")
		print('----------------------------------')

def main():
	print("====================================================")
	print("===== Check if the string is palindrome or not =====")	
	print("====================================================")	
	response=input("Please enter your string:")
	print("Your string is:",response.upper())
	method1(response)
	method2(response)

if __name__=='__main__':
	main()	

