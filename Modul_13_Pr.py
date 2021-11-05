numbers = int(input("Сколько билетов вы хотите приобрести: ")) #Кол-во билетов
age = [int(input("Введите возраст: ")) for i in range(numbers)]
print()
free = len([x for x in age if x < 18])*0
discount = len([x for x in age if 18 <= x < 25 ])*990
full = len([x for x in age if x >= 25])*1390
price = free + full + discount
if numbers >= 3:
    sales = int(price - price*0.1)
    print("Сумма к оплате:" ,sales)
else:
    print("Сумма к оплате:" ,price)
