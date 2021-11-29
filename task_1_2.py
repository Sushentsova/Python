list_of_num = []
number = 1

while number <= 1000:
    if number % 2 == 0:
        list_of_num.append(number ** 3)
    number += 1
print(list_of_num)

list_of_sum = []
sum_of_num = 0
for num_3deg in list_of_num:
    sum_of_num = sum_of_num + num_3deg % 10
    num = num_3deg // 10
    if sum_of_num % 7 == 0:
        list_of_sum.append(sum_of_num)
print(list_of_sum)

result = 0
for sum_of_num in list_of_sum:
    result += sum_of_num
print(result)

new_list_of_num = []
new_sum_of_num = 0
for num in list_of_num:
    new_num = num + 17
    new_list_of_num.append(new_num)
print(new_list_of_num)

new_list_of_sum = []
new_sum_of_num = 0
for new_num in new_list_of_num:
    new_sum_of_num = new_sum_of_num + new_num % 10
    num = new_num // 10
    if new_sum_of_num % 7 == 0:
        new_list_of_sum.append(new_sum_of_num)
print(new_list_of_sum)

new_result = 0
for new_sum_of_num in new_list_of_sum:
    new_result += new_sum_of_num
print(new_result)
