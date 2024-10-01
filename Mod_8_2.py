def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for i in numbers:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Incorrect data input - {i}')
    return result, incorrect_data


def calculate_average(numbers):
    try:
        result_ps = personal_sum(numbers)
        sum_numbers, incorrect_datatypes = result_ps
        amount_elements = len(numbers) - incorrect_datatypes  # For acting with only integers
        am_average = sum_numbers / amount_elements
        return am_average

    except ZeroDivisionError:
        return 0

    except TypeError:
        print('Incorrect data type in numbers')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
