#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
x = 4
y = 4
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            n = int(input(f"Enter first number: "))
            c = int(input(f"Enter second number: "))
            if n == i and c == j:
                print('You guessed:)')
            else:
                print('You did not guess right:(')
#Я знаю что есть ошибка. При вводе 5, 6 код берет сначала 2,3, потом 3,2. Отрабатывает 2 раза. Хотел усложнить себе задачу.