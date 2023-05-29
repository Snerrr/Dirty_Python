# 6. Проверка на палиндром:
#    а. слова

slovo = str(input("Введите слово: "))
flag = 0

for i in range(len(slovo)):
    if slovo[i] != slovo[-i - 1]:
        flag += 1
if flag == 0:
    print("Это слово палиндром")
else:
    print("Это слово не является палиндромом")
