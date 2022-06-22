from collections import Counter
import time

def calculate_time(func):
	def wrapper(*args,**kwargs):
		start=time.time()
		result=func(*args,**kwargs)
		end=time.time()
		print("Time taken for this method to complete is:"+str((end-start)*1000)+" mil sec")
		return result
	return wrapper

@calculate_time
def method_loop(value1,value2):
	print("==============================")
	print("Anagrams Using the looping")
	print("==============================")	
	result=True
	for char in value1:
		if char not in value2:
			result=False
	if result:
		print("***** The strings are angrams!! *****")
	else:
		print("***** The strings are not angrams!! *****")			

@calculate_time
def method_set(value1,value2):
	value1 = value1.replace(' ', '')
	value2 = value2.replace(' ', '')
	print("==============================")
	print("Anagrams Using the sets")
	print("==============================")
	if set(value1) == set(value2):
		print("***** The strings are angrams!! *****")
	else:
		print("***** The strings are not angrams!! *****")		

@calculate_time
def method_counter(value1,value2):
	print("==============================")
	print("Anagrams Using the counter from functools")
	print("==============================")
	value1 = value1.replace(' ', '')
	value2 = value2.replace(' ', '')
	counter1=Counter(value1)
	counter2=Counter(value2)
	if counter1 == counter2:
		print("***** The strings are angrams!! *****")
	else:
		print("***** The strings are not angrams!! *****")


def main():
	value1=input("Enter the first string:")
	value2=input("Enter the second string:")
	print("The values entered are {v1} and {v2}".format(v1=value1,v2=value2))
	method_counter(value1,value2)
	method_set(value1,value2)
	method_loop(value1,value2)

if __name__ == '__main__':
	main()	