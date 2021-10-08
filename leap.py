def find_year(year):
	if (year % 4) == 0:
		if (year % 100) == 0:
			if (year % 400) == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

year = input("Enter year ")
year = int(year)
if(find_year(year)):
	print("it is a leap year")
else:
	print("it is not a leap year")