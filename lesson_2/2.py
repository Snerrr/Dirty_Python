# 2. Какого цвета клетка
# На вход подается обозначение шахматной клетки, необходимо вывести ее цвет

alphabet = {
           "A" : 1,
           "B" : 2,
           "C" : 3,
           "D" : 4,
           "E" : 5,
           "F" : 6,
           "G" : 7,
           "H" : 8, 
           }
position = str(input("Введите позицию: "))
if alphabet[position[0]] % 2 == int((position[1])) % 2:
    print(f"{position} - Black")
else:
    print(f"{position} - White")
