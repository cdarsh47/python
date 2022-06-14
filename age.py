import datetime
import math

def main():

	datetime_obj=datetime.date.today()

	bday=input('Please enter your birthday in y-m-d format:')
	datetime_bday=bday.split('-')
	byear=datetime_bday[0]
	bmonth=datetime_bday[1]
	bday=datetime_bday[2]

	if len(byear) > 4:
		raise ValueError("Please enter proper year value.")
	if int(bmonth) > 12:
		raise ValueError("Months value cant have more than 12")
	if int(bday) > 31:
		raise ValueError("Days value cant have more than 31")	

	datetime_bday=datetime.date(int(byear),int(bmonth),int(bday))	

	print("You are {age} years old".format(age=math.floor((datetime_obj - datetime_bday).days / 365)))

if __name__ == '__main__':
	main()
