per_center = {'ТКБ':5.6,'СКБ':5.9,'ВТБ':4.28,'СБЕР':4.0}
money = int(input("Введите сумму:"))
print(money)
TKB = int((per_center['ТКБ']) * (money/100))
SKB = int((per_center['СКБ']) * (money/100))
VTB = int((per_center['ВТБ']) * (money/100))
SBER = int((per_center['СБЕР']) * (money/100))
deposit = [TKB, SKB, VTB, SBER]
print("Накопленные средства за год вклада в каждом из банков =",deposit)
print("Максимальная сумма, которую вы можете заработать:", max(deposit))