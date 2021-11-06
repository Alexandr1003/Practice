numbers = int(input("Сколько билетов вы хотите приобрести: ")) #Кол-во билетов
age = [int(input("Введите возраст: ")) for i in range(numbers)] #Возраст покупателей 
print()
free = len([x for x in age if x < 18])*0 #Цена для лиц младше 18 лет
discount = len([x for x in age if 18 <= x < 25 ])*990 #Цена для лиц от 18 до 25 лет
full = len([x for x in age if x >= 25])*1390 #Цена для лиц от 25 лет
price = free + full + discount 
if numbers > 3: #Скидка 10% если больше 3 билетов
    sales = int(price - price*0.1)
    print("Сумма к оплате со скидкой 10% :" ,sales)
else: 
    print("Сумма к оплате:" ,price)
