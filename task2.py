# Напишите программу, которая получает на вход строку чисел, разделенных пробелами, и формирует словарь,
#  в котором ключами служат числа, а значениями – слово "четное" или "нечетное".
numbers_input = input("Введите числа через пробел: ")
numbers = list(map(int, numbers_input.split()))
result = {}
for num in numbers:
    if num % 2 == 0:
        result[num] = "четное"
    else:
        result[num] = "нечетное"
print(result)
