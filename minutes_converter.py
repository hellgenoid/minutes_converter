# Эта функция высчитывает количество дней из количества часов
def check_hours(time):
    days = 0
    while time > 24:
        time = time - 24
        days += 1
    if time == 24:
        time = '00'
        days += 1
    elif time < 10:
        time = '0' + str(time)
    return time, days


while True:
    try:
        time_now = int(input("Чтобы выйти из программы введите цифру 0.\nВведите количество минут: "))
        minutes = time_now % 60
        hours = time_now // 60
        if minutes < 10:
            minutes = '0' + str(minutes)
        hours_now, days_now = check_hours(hours)
        if time_now == 0:
            break
        else:
            print(f"\n{days_now} дней, {hours_now}:{minutes}\n")
    except ValueError:
        print("\nОшибка! Вводите только цифры.\n")
