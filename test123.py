Модуль 1 Часть 1:

Уровень 1

value = (5 + (7 * 5 / 8)) / 3**5
print(value)

Уровень 2

a = 109
v = int(input("Введите скорость км в час: "))
t = int(input("Введите время в пути: "))
x = v * t
d = x % 109
g = (a > x) * x + (x > a) * d + (x == a) * a
print(g)


Уровень 3

a = float(input("Введите первое число: "))
b = float(input("Ввелите второе число :"))
x = (a > b) * a + (b >= a) * b
print("Наибольшее число: ", x)

Модуль 1 Часть 2

Уровень 1

t1 = int(input("Введите первое число: "))
t2 = int(input("Введите второе число: "))
t3 = int(input("Введите третье число: "))
if t1 == t2 == t3:
print(3)
elif t1 == t2:
print (2)
elif t1 == t3:
print (2)
elif t2 == t3:
print (2)

else:
print(0)

Уровень 2

t1 = int(input("Введите первое число: "))
t2 = int(input("Введите второе число: "))
t3 = int(input("Введите третье число: "))
t4 = int(input("Введите четвертое число: "))
if t1 == t3:
print("YES")
elif t2 == t4:
print ("YES")
else:
print ("NO")

Уровень 3

x = input("Придумайте пароль: ")
t1 = x.isupper()
t2 = x.islower()
t3 = len(x)
if t1 == 0 and t2 == 0 and t3 >= 8:
print("Пароль успешно создан")
else:
print("Не соблюдены условия пароля")