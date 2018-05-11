#CONSTANTS
GPA_CONV_LIST = [
	"A+",4.0,
"A", 4.0,
	"A-", 3.7,
	"B+", 3.3,
	"B", 3.0,
	"B-", 2.7,
	"C+", 2.3,
	"C", 2.0,
	"C-", 1.7,
	"D+", 1.3,
	"D", 1.0,
	"F", 0 
	]

def harvestInput():
	retList = []
	while True:
		grade = input("Enter Grade or press ONLY ENTER to quit: ")
		if grade != "":
			retList.append(grade.upper())
		else:
			return retList

def ltn(letterGrades, resource):
	retList = []
	for i in letterGrades:
		thingToAppend = resource[resource.index(i)+1]
		retList.append(thingToAppend)
	return retList

def avg(arg):
	return sum(arg)/len(arg)
	
def welcome():
	print("Welcome to MCPS Portal")
	print("This utility was designed for our more...")
	print("Tech savy teachers to calculate their...")
	print("Grades on a terminal or Command Prompt...")
	print("Please enter your data below: ")
	
def main():
	welcome()
	dat = [input("Please enter one letter grade: ").upper()]
	dat = ltn(dat,GPA_CONV_LIST)
	print("The grade is: ")
	print(dat)

main()
	
	
	
	
	
