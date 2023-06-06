# 3. Дан список чисел. Создать новый список, 
# который будет содержать только уникальные элементы исходного списка
from random import randint
print(my_list := [randint (0,20) for i in range(20)])
print(my_list1 := sorted(set(my_list)))
