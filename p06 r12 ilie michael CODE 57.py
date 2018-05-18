year = int(input("Enter year: "))

if year %4 ==0 and year %400 ==0 and year %100 != 0:
      print("Leap year")
else:
  print("year is not Leap")
  
