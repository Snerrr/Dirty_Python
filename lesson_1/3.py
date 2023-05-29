# 3. На вход поступает число: найти сумму цифр числа, 
# в том числе если оно отрицательное или вещественное.
summa = 0
chislo = list(input("Введите число: "))
if chislo[0] != "-":
  for i in range (len(chislo)):
      if chislo[i] != ".":
        summa += int(chislo[i])
  print(summa)
elif chislo[0] == "-":
  for i in range (1,len(chislo)):
      if chislo[i] != ".":
        summa += int(chislo[i])
  print(summa) 
