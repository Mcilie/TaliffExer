def days(month, year):
  if year %4 ==0 and year %400 ==0 and year %100 != 0 and month == 2:
    print("DAYS: %d" % 29)
  else:
    monthq = {1,"January", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}[month]
    if monthq in ['September', 'April', 'June', 'November']:
        print("DAYS: %d" % 30)

    elif monthq in ['January', 'March', 'May', 'July', 'August','October','December']:
        print("DAYS: %d" % 31)  
        
def main():
  year = int(input("Enter year: "))
  month = int(input("Enter number of month: "))
  days(month,year)
  
main()
