def binary_search(arr_number, search_num):
	low = 0  
	high = len(arr_number) - 1  
	middle = 0

	while low <= high:

		middle = (high + low) // 2

		if arr_number[middle] < search_num:
			low = middle + 1 

		elif arr_number[middle] > search_num:
			high = middle - 1

		else:
			return middle
	return -1 

def main():
	print("===============================")
	print("This is a binary search program")
	print("===============================")

	resp=input("enter comma separated values to sort the numbers(1,2,3,4):")
	search_num=int(input("Please enter the number to search:"))
	if resp and search_num:
		arr_number=sorted([int(i) for i in resp.split(',')])
		print("The sorted list is:",arr_number)
		result = binary_search(arr_number, search_num)  
		if result != -1:  
			print("Element is present at index", str(result))
		else:  
			print("Element is not present in the list")	

if __name__ == '__main__':
	main()
