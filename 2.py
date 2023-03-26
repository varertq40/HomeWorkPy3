# 3.2[18]: Требуется найти в списке целых чисел самый близкий
# по величине элемент к заданному числу X. Пользователь вводит
# это число с клавиатуры, список можно считать заданным. 
# Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10

list_integers = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
list_integers.sort()
# [2, 3, 3, 3, 5, 5, 7, 7, 8, 10]
job_search_value = int(input('Введите целое число: '))

closest_element = 0
for i in range(len(list_integers)):
    if list_integers[i] >= job_search_value:
        closest_element = list_integers[i]
        print(closest_element)
        break
