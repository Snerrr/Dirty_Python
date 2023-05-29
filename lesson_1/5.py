# Дана строка текста, необходимо сформировать из нее две новых строки из символов 
# которые стоят на четных позициях и на нечетных

chet = []
nechet = []
text = str(input("Введите текст: "))
for i in range(0 , len(text) , 2):
    nechet.append(text[i])
for i in range(1 , len(text) , 2):
    chet.append(text[i])
print("строка с нечётными позициями: ")
print(str("".join(map(str, nechet))))
print("строка с чётными позициями: ")
print(str("".join(map(str, chet))))
