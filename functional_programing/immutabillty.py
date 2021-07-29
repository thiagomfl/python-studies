from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce


setlocale(LC_ALL, 'pt_BR')

month_31 = filter(lambda month: mdays[month] == 31, range(1, 13))
month_names = map(lambda month: month_name[month], month_31)
concat_names = reduce(lambda all_months, name_month: f'{all_months}\n- {name_month}', month_names, 'Months with 31 days:')
print(concat_names)
