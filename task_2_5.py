# задание 5
prices = [57.8, 46.51, 97, 7, 45.8, 9.97, 34, 44.5, 23, 85.34, 76]
print('Список цен:', prices, 'ID: ', id(prices))

print('Задание А:')
for i in prices:
    print(f'{int(i):01} руб. и {int(i * 100 % 100):01} коп.', end=", ")

print('Задание B:')
prices.sort()
print('Список после сортировки', prices, 'ID: ', id(prices))

print('Задание С:')
prices_reversed = sorted(prices, reverse=True)
print('Новый список:', prices_reversed, 'ID: ', id(prices_reversed))

print('Задание D:')
print('Цены пяти самых догрогих товаров:', prices_reversed[:4])