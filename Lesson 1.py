# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.
#         *Пример:*
#         - 6 -> да
#         - 7 -> да
#         - 1 -> нет




day = int(input('введите день недели '))

if day <= 5:
    print("нет")
elif 6 <= day <= 7:
    print("да")




# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.




x, y, z = int(input()), int(input()), int(input())

if not(x or y or z) == (not x and not y and not z):
    print("True")
else:
    print("False")




# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
# плоскости, в которой находится эта точка (или на какой оси она находится).
# Для тех кто пропусти модули с алгоритмами: ¬ - это Отрицание (не); ⋁ - Дизъюнккия (или) ; ⋀ - Конъюнкция (и)
# Пример:
#         - x=34; y=-30 -> 4
#         - x=2; y=4-> 1
#         - x=-34; y=-30 -> 3




x, y = int(input()), int(input())

if x > 0 and y > 0:
    print('I')
elif x < 0 and y > 0:
    print('II')
elif x < 0 and y < 0:
    print('III')
elif x > 0 and y < 0:
    print('IV')




# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).




num = int(input('Введите номер четверти: '))
if num == 1:
    print('координата х от 0 до бесконечности, а координата y от 0 до бесконечности')
elif num == 2:
    print('координата х от 0 до минус бесконечности, а координата y от 0 до бесконечности')
elif num == 3:
    print('координата х от 0 до минус бесконечности, а координата y от 0 до минус бесконечности')
elif num == 4:
    print('координата х от 0 до бесконечности, а координата y от 0 до минус бесконечности')
else:
    print('не верный номер четверти')




# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21




a = list(input())
b = list(input())
a_new = []
b_new = []
for i in a:  # можно и без нового списка, просто указать срез a_new[2]
    if i != ',':
        a_new.append(i)
for i in b:
    if i != ',':
        b_new.append(i)

distance = ((int(b_new[0]) - int(a_new[0]))**2 + (int(b_new[1]) - int(a_new[1]))**2)**0.5
print(round(distance, 3))
