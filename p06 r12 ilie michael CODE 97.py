import random

def genPass():
  retvar =""
  for i in range(random.randint(1,15)):
    retvar+=chr(random.randint(33,126))
  print(retvar)
  return retvar

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
  steps = 1
  while True:
    pas = genPass()
    if goodPass(pas): 
      print("Steps taken: %d" % steps)
      break
    else:
      steps +=1
main()
