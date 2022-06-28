from collections import Counter

def main():
	
	print("=================================================")
	
	print("Welcome to the string matching/comparison program")
	
	print("=================================================")

	first_string=input("Please enter the first string:")
	
	second_string=input("Please enter the second string:")

	if first_string and second_string:
	
		match_total,common_dict=0,{}
	
		total_count=len(first_string)+len(second_string)
	
		dict_1=dict(Counter(first_string))
	
		dict_2=dict(Counter(second_string))
	
		for key,value in dict_1.items():
	
			if key in dict_2:
	
				if value != dict_2[key]:
	
					if value > dict_2[key]:
	
						inc=dict_2[key]
	
					else:
	
						inc=value
	
					match_total += inc
	
					common_dict.update({key: inc*2})
	
				else:			
	
					common_dict.update({key: dict_2[key]*2})
	
					match_total += dict_2[key]
	
		match_count = match_total * 2
	
		if match_count == total_count:
	
			print("====================  Result  =========================")
	
			print("=======================================================")		
	
			print(f"Both the words are similar and have same character count.")
	
			print("=======================================================")	
	
		else:
	
			print("====================  Result  =========================")
	
			print("=======================================================")			
	
			print(f"Out of total of {total_count} chracters, {match_total * 2} characters are similar between the strings(including the spaces).")
	
			print("=======================================================")
	
			print("Common characters and number of occurrences between the strings:")

			print(common_dict)

if __name__ == '__main__':
	main()		
