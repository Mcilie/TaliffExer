lista = []
d = input("ENTER WORD: ")
while d!='':
  if d not in lista: lista.append(d.lower())
  d = input("ENTER WORD: ")
print(lista)
