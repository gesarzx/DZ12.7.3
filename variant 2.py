per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=float(input('введите сумму вклада:'))

deposit=[money/100*i for i in per_cent.values()]

print('доход=', deposit)
print("максимальный доход=", round(max(deposit),2))