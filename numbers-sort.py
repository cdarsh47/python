def sort_function(numbers):
	
	length,i=len(numbers),0
	
	while i<length:
	
		j=0
	
		while j<=length-2:
	
			try:
	
				if numbers[j] and numbers[j+1] and numbers[j] > numbers[j+1]:
	
					numbers[j],numbers[j+1]=numbers[j+1],numbers[j]			
	
			except:
	
				print("Done")
	
			j+=1
	
		i+=1;
	
	return numbers

def main():
	
	print("=======================================")
	
	print("Welcome to the sorting numbers program.")
	
	print("=======================================")
	
	numbers=input("enter comma separated values to sort the numbers(1,2,3,4):")
	
	numbers_list=[int(number) for number in numbers.split(',')]

	print("----------------------------------------------")

	print("Unsorted list of numbers:",numbers_list)

	print("----------------------------------------------")
	
	sorted_list=sort_function(numbers_list)
	
	print("==============================================")
	
	print("Here is the sorted numbers list:",sorted_list)

	print("==============================================")

if __name__ == '__main__':
	main()