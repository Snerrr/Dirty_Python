# 1. На вход подается число с плавающей точкой, выведите первую цифра дробной части
# 13.152
# 1

chislo = float(input("Введите число: "))
if chislo >= 1 or chislo == -1:
  celoe = chislo // 1
  pervay = chislo % celoe * 10
  print(int(pervay)) 
elif chislo <= -1:
  celoe = chislo // 1 + 1
  pervay = chislo % celoe * 10
  print(int(pervay))
elif -1 < chislo < 1:
  pervay = chislo * 10
  print(int(pervay))