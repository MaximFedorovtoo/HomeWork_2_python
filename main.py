import math
from random import randint


# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые 
# – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
#  были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

def space():
    print('')
    print('')

def task_1():
    print('Задача 10')
    n = int(input("Введите количество монеток "))
    heads = 0
    tails = 0
    coins = []
    for i in range(n):
        coins.append(randint(0,1))
        if coins[i] == 0:
            heads+=1
        else:
            tails+=1
    print(f'Монеты лежат в таком порядке {coins}, где 0 - орел, 1 - решка ' )
    if heads < tails:
        print(f'Переверните {heads} монеты лежащие орлом')
    else:
        print(f'Переверните {tails} монеты лежащие решкой')

    
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.


def task_2():
    print('Задача 12')
    summ = int(input('Введите сумму чисел '))
    product = int(input('Введите произведение чисел '))
    first_numb = 0
    second_numb = 0
    for i in range(summ):
        for j in range(summ):
            if i+j == summ and i*j == product:
                first_numb = i
                second_numb = j
    print(f'Первое число равно {first_numb}, второе число равно {second_numb}')
    space()
    print('Еще одно решение менее загружающее систему')
    first_numb = int(((summ + math.sqrt(summ*summ-(4*product)))/2))
    second_numb = int(((summ - math.sqrt(summ*summ-(4*product)))/2))
    print(f'Первое число равно {first_numb}, второе число равно {second_numb}')
    


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


def task_3():
    print('Задача 14')
    limit = int(input("Введите число N "))
    degree = 2
    while degree < limit:
        print(degree)
        degree*=2
    
      
def main():
    task_1()

    space()
    task_2()
    space()
    task_3()


if __name__ == '__main__':
    main()