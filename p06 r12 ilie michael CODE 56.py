text = int(input("Enter number of texts sent this month: "))
mins = int(input("Enter the number of minutes called this month: "))
textOver,minsOver = 0,0

print("Base charge: %.2f" % 15)
if text > 50:
  textOver = .15*(text-50)
  print("Text fee: %.2f" % textOver)
if mins > 50:
  minsOver = .25*(mins-50)
  print("Minute fee: %.2f" % minsOver)

totalBefore911=textOver+15+minsOver

print("911 fee: .44")
total =  .44 + totalBefore911

print("Tax : %.2f" % (.5*total))
print("Total: %.2f" % ((.5*total) + total))
