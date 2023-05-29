# 4. На вход поступает десятичное число, вывести его в виде двоичного

chislo = int(input("Введите десятичное число: "))
dvoich = []
if chislo > 0:
    while chislo > 0:
        dvoich.append(chislo % 2)
        chislo //= 2
    dvoich = dvoich[::-1]
    print(str("".join(map(str, dvoich))))
elif chislo < 0:
    chislo *= -1
    while chislo > 0:
        if chislo % 2 == 0:
             dvoich.append(1)
             chislo //=2
        else:
            dvoich.append(0)
            chislo //= 2
    dvoich = dvoich[::-1]
    print(str("".join(map(str, dvoich))))
else:
    print(0)

