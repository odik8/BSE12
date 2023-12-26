def count_and_sum_recursive(numbers, index=0, count=0, total_sum=0):
    if index == len(numbers):
        return count, total_sum

    current_number = numbers[index]
    if current_number < 0:
        return count, total_sum
    else:
        count += 1
        total_sum += current_number
        return count_and_sum_recursive(numbers, index + 1, count, total_sum)


if __name__ == "__main__":
    numbers_list = list(map(float, input("Вводите числа через пробел: ").split()))
    result_count, result_sum = count_and_sum_recursive(numbers_list)

    print("Количество чисел:", result_count)
    print("Сумма чисел:", result_sum)
