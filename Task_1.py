# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_week = int(input('Введите цифру, обозначающую день недели: '))
if day_week < 1:
    print('Число не может быть отрицательным или равняться нулю.')
elif day_week > 7:
    print(f'В неделе не может быть {day_week} дней.')
elif 0 < day_week < 6:
    print('Это будний день.')
else:
    print('Ура! Этот день выходной!')
