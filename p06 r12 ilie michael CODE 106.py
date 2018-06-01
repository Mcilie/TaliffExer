def remOut(q, num):
  l = sorted(q)
  sortdict ={}
  for i in range(len(l));
    sortdict[i] = l[i]
  for i in sortdict:
    if i<num or i> len(l)-num:
      print("Removed %d" % sortdict[i])
      sortdict[i] = ''
  retlist = []
  for i in sordict:
    if sortdict[i] != '':
      retlist.append(sortdict[i])
  return retlist
  
def main():
  bigList = []
  d = input("Enter a number or just press enter to quit: ")
  while d!='':
    bigList.append(float(d))
    d = input("Enter a number or just press enter to quit: ")
  if len(bigList) < 4: print("ERROR, must be atleast 4 nums!!")
  else:
    print("Your list w/ out outliers: ", remOut(bigList, 2)
  
main()
      
