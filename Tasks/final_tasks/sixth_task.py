# 6.	Аренда ракет
# Вы – компания, дающая в аренду ракеты. Каждый день к вам приходит список заявок на использование ракет в виде:
# (час_начала, час_конца), (час_начала, час_конца), ...
# Если аренда ракеты заканчивается в час X, то в этот же час ее уже можно взять в аренду снова
# (т.е. час_начала может начинаться с Х).
# Дано: список заявок на использование ракет
# Задача: вывести ответ, хватит ли вам одной ракеты, чтобы удовлетворить все заявки на этот день


def count_working_hours(applications: list, working_hours=12) -> bool:
    begining = [i[0] for i in applications]
    finish = [i[1] for i in applications]
    app_hours = (finish[-1] - begining[-1])

    while True:
        for i in range(len(finish)-1):
            if finish[i] <= begining[i+1]:
                app_hours += (finish[i] - begining[i])
                if app_hours > working_hours:
                    return False
            else:
                return False
        return True


if __name__ == '__main__':
    apps = [(10, 13), (13, 17), (18, 20)]
    print(count_working_hours(apps))