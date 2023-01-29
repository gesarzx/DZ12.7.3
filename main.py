per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money=float(input('введите сумму вклада:'))

deposit=[]
deposit.append(money/100*per_cent['ТКБ'])
deposit.append(money/100*per_cent['СКБ'])
deposit.append(money/100*per_cent['ВТБ'])
deposit.append(money/100*per_cent['СБЕР'])

print('доход=', deposit)
print("максимальный доход=", round(max(deposit),2))

