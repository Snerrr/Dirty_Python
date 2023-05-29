# 2. На вход подается целое число, необходимо поменять местами первую и последняя цифру в числе
# 105
# 501

chislo = list(input("Введите число: "))
if chislo[0] != "-":
  chislo[0] , chislo[-1] = chislo[-1] , chislo[0]
else:
  chislo[1] , chislo[-1] = chislo[-1] , chislo[1]
print(int("".join(map(str, chislo))))
