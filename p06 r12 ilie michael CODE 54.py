def waveLength(number):
	theDict={
			450:"Violet",
			495:"Blue",
			570:"Green",
			590:"Yellow",
			620:"Orange",
			751:"Red"}
	if number < 380 or number > 751:
		return "INVALID WAVELENGTH"
	for i in theDict:
		if number < i:
			return theDict[i]
			
def main():
	var = float(input("Please enter waveLenght: "))
	print(waveLength(var))
	
main()
