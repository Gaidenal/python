duration = int(input("Введите целое число и нажимите 'Enter': " ))
if 0 <= duration < 60:
    print(duration, "сек\n")
elif 60 <= duration < 3600:
    min = duration // 60
    sec = duration - min * 60
    print(min, "мин ", sec, "сек\n")
elif 3600 <= duration < 86400:
    hour = duration // 3600
    min = (duration - hour * 3600) // 60
    sec = duration - hour * 3600 - min * 60
    print(hour, "час", min, "мин ", sec, "сек\n")
elif  duration >= 86400:
    day = duration // 86400
    hour = (duration - day * 86400) // 3600
    min = (duration - day * 86400 - hour * 3600) // 60
    sec = duration - day * 86400 - hour * 3600 - min * 60
    print( day, "дн", hour, "час", min, "мин ", sec, "сек\n")
else:
    print("Вы ввели некорректное число. Пожалуйста,попробуйте заново.")