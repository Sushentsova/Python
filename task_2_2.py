# задание 2
weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

weather_new = []
for i, s in enumerate(weather):
    if s.isdigit():
        weather[i] = f'{s[0]:01}'
        weather_new.append(s)
    elif s[1:].isdigit():
        weather[i] = f'{s[1]:01}'
        weather_new.append(s)
    else:
        weather_new.append(s)
print(weather_new)