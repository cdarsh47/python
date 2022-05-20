#A different arithmetic operator resulting values program using the generator function.
def operation_generator(x,operation,mode):
		
		#yield x

		limit,incrementor = 5,1

		if operation=='exponent':
			while incrementor<=limit:
				if(mode.lower()=='continuous'):
					x=x*x
					incrementor+=1
					yield x
				else:
					resp=input("do you wish to continue?(y/n):")
					if(resp.lower()=='y'):
						x=x*x
						incrementor+=1
						yield x
					else:
						print("Program running done!!")	
						break;
			
		elif operation=='addition':
			while incrementor<=limit:
				if(mode.lower()=='continuous'):
					x=x+1
					incrementor+=1
					yield x
				else:	
					resp=input("do you wish to continue?(y/n):")
					if(resp.lower()=='y'):
						x=x+1
						incrementor+=1
						yield x
					else:
						print("Program running done!!")	
						break;
		elif operation=='fibonacci':
			x,y=0,1
			print(str(x)+"\n"+str(y)+"\n"+str(x+y))
			while incrementor<=limit:
				if(mode.lower()=='continuous'):
					fib=lambda x,y:x+y
					x,y=y,x+y
					last_num=fib(x,y)
					incrementor+=1
					yield last_num
				else:
					resp=input("do you wish to continue?(y/n):")
					if(resp.lower()=='y'):
						fib=lambda x,y:x+y
						x,y=y,x+y
						last_num=fib(x,y)
						incrementor+=1
						yield last_num
					else:	
						print("Program running done!!")	
						break;

#result=exponent_generator(2)

print("========================================")
print("Do you need the whole output to show at once or you need to be prompted to continue?")
print("")
mode=input("Please input out of the two values: continuous or prompt ->")
print("========================================")
print("Select one of the options shown below to perform operation:")
print("========================================")
print("Type 1 for getting exponent:Exponent")
print("Type 2 for addition values:Addition")
print("Type 3 for addition values:fibonacci")
print("========================================")

response=input("Please enter your input:")
print('========================')
if response=='1':
	result=operation_generator(2,'exponent',mode)
elif response=='2':	
	result=operation_generator(1,'addition',mode)
elif response=='3':
	result=operation_generator(3,'fibonacci',mode)	
else:
	print("Either it is bad value enetered or the value does not fall in above mention range.")			

for value in result:
	print(value)

