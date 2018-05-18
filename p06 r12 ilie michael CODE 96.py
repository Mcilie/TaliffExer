def goodPass(pas):
  l = 0
  u = 0
  n = 0
  for i in pass:
    if i.isupper(): u +=1
    if i.isdigit(): n +=1
    if i.islower(): l +=1
  return len(pas)>7 and (l*u*n) != 0
  
  def main():
    pas = input("Enter password: ")
    if goodPass(pas):
      print("STRONG PASSWORD")
    else:
      print("WEAK PASSWORD")
      
if __name__ == "__main__":
  main()
