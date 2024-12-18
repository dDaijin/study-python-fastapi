# Перевірка паролю
password = 'qwert123'

if password == 'qwert123':
    print('Ви увійшли в систему')
else :
    print('Неправильний пароль')

# Визначення днів тижня
week_day = 1, 'Monday'

if 1 in week_day :
    print(week_day)
else :
    print('Error')

# Цикли
# Таблиця множення
x = 3
y = 1

while y < 11:
    print(x*y)
    y = y + 1

# Сума чисел
list = [2, 5, 7, 9,45]
sum = 0

for nun in list:
    sum = nun+sum
    print(sum)

# Факторіал числа
x = 5
f = 1

while x > 1:
    f = f * x
    x = x-1
    print(f)

# Парні числа
x = 1
y = 2

while x <= 25:
    print(y*x)
    x = x + 1

# Пошук простих чисел
list = [1, 3, 5, 4, 6, 8]
result = []
n= 2

for i in list:
    if i % 2==0:
        break
    else :
        result.append(i)
print(result)