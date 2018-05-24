def days(month, year):
  if year %4 ==0 and year %400 ==0 and year %100 != 0 and month == 2:
    return 29
  else:
    monthq = {1:"January", 2:"February",3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}[month]
    if monthq in ['September', 'April', 'June', 'November']:
        return 30

    elif monthq in ['January', 'March', 'May', 'July', 'August','October','December']:
        return 31
    else: return 28
  
def speshalday(day, month, year):
	if day*month == int(str(year)[2:]): return True
	return False

def main():
  for i in range(1900,2000):
    for j in range(12):
      daysOfMonth = days(j+1,i)
      for _ in range(daysOfMonth):
        if speshalday(_+1, j+1, i):
          month = monthq = {1:"January",2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}[j+1]
          print(month, _+1, i)
main()
