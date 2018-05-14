coefficient = int(input("Enter the coefficient: "))
power = int(input("Enter the power of 10: "))
num = coefficient * 10 ** power

var = num
if var < 3*10**9:
  print("Radio Wave")
elif var <3*10**12:
  print("MicroWaves")
elif var < 4.3 * 10**14:
  print("Infrared Light")
elif var < 7.5 * 10 ** 14:
  print("Visible Light")
elif var < 3 * 10 ** 17:
  print("UltraViolet Light")
elif var < 3 * 10 ** 19:
  print("X-rays")
else:
  print("Gamma rays")
  
  
