why = []
q = int(input("Enter Element to enter to list (0 terminates program): "))
while q!=0:
  why.append(q)
  q = int(input("Enter Element to enter to list (0 terminates program): "))
for i in sorted(why)[::-1]: print(i)
