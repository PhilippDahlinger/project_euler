

def check_year(y, start_day, current_count):
    num_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if y % 4 == 0:
        num_days[1] += 1
    for month, len_month in enumerate(num_days):
        if start_day == 6:
            current_count += 1
        start_day = (start_day + len_month) % 7
    return current_count



def get_start_days():
    y = 1900
    cur_day = 0
    result = {}
    while y < 2001:
        if y % 4 == 0:
            if y != 1900:
                # leap year
                num_days = 366
            else:
                num_days = 365
        else:
            num_days = 365
        result[y] = cur_day
        y += 1
        cur_day = (cur_day + num_days) % 7
    return result


start_days = get_start_days()
current_count = 0
for (k,v) in start_days.items():
    if k == 1900:
        continue
    current_count = check_year(k, v, current_count)
print(current_count)

