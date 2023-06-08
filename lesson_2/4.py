# 4. Принимаем с консоли число и выводим две последовательности Фибоначчи и Негафибоначчи 
# (можно прочитать в wiki что это)
# Пример: Вводим 8
# [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Fn = Fn–2 + Fn–1

chislo = int(input("Введите число: "))
my_list = [0, 1]
for i in range(2, chislo + 1):
    my_list.append(my_list[i - 2] + my_list[i - 1])
my_list1 = my_list[1:].copy()
for i in range(1, chislo, 2):
    my_list1[i] *= -1
print(my_list1[::-1] + my_list)