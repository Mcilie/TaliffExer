p  = str(input("ENTER PLATE : "))

if len(p) == 6:
  if (p[0].isupper() and p[1].isupper() and p[2].isupper()) and (p[3].isdigit() and p[4].isdigit() and p[5].isdigit()):
    print("Valid old license plate")
  else:
    print("INVALID")
elif len(p) == 7:
  if (p[0].isdigit() and p[1].isdigit() and p[2].isdigit() and p[3].isdigit()) and (p[4].isupper() and p[5].isupper() and p[6].isupper()):
    print("VALID NEW LICENSE")
  else:
    print("INVALID")
else:
  print("INVALID")
