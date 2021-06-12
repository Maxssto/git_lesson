from random import randint
numbers = int(input("Сколько элементов в списке: "))
lst = []
for num in range(numbers):
    lst.append(randint(1, 100))
lst_sorted = sorted(lst)
print("Рандомный список:", lst)
print("Отсортированный список:", lst_sorted)


