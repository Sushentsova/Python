number = 1
while number <= 100:
    digit = number % 10
    if digit == 1 and number != 11:  # все цифры оканчивающиеся на 1
        print(number, 'процент')
    elif 2 <= digit <= 4:  # все цифры оканчивающиеся на 2, 3, 4
        print(number, 'процента')
    else:
        print(number, 'процентов')
    number += 1
