number_of_orders = int(input())
total_price = 0
for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        total_price_per_order = price_per_capsule * days * capsules_per_day
        print(f'The price for the coffee is: ${total_price_per_order:.2f}')
        total_price += total_price_per_order

print(f'Total: ${total_price:.2f}')



# # Инициализираме общата цена
# обща_цена = 0
#
# # Прочитаме броя на поръчките
# брой_поръчки = int(input())
#
# # Обработваме всяка поръчка
# for _ in range(брой_поръчки):
#     # Прочитаме данните за поръчката
#     цена_на_капсула = float(input())
#     дни = int(input())
#     капсули_на_ден = int(input())
#
#     # Проверяваме дали входните стойности са в зададените интервали
#     if 0.01 <= цена_на_капсула <= 100.00 and 1 <= дни <= 31 and 1 <= капсули_на_ден <= 2000:
#         # Изчисляваме общата цена за поръчката
#         обща_цена_за_поръчка = цена_на_капсула * дни * капсули_на_ден
#         print(f"Цената за кафето е: ${обща_цена_за_поръчка:.2f}")
#         обща_цена += обща_цена_за_поръчка
#
# # Извеждаме общата цена
# print(f"Общо: ${обща_цена:.2f}")
#
