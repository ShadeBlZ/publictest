import json

with open("orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)

#1
max_price = 0
max_order = ''
for order_num, orders_data in orders.items():
    price = orders_data['price']
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')

#2
max_quantity = 0
max_order = ''
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        max_quantity = quantity
        max_order = order_num
print(f'Номер заказа с самым большим количеством товаров: {max_order}')


#3
date_dict = {}
for order_num, order_data in orders.items():
    date = order_data['date']
    date_dict[date] = date_dict.get(date, 0) + 1

for date in sorted(date_dict):
    max_value = max(date_dict.values())
    if date_dict[date] == max_value:
        print(f'Больше всего заказов было сделано {date}: {date_dict[date]}')

#4
max_orders = 0
user_dict = {}
for order_num, order_data in orders.items():
    user_id = order_data['user_id']
    user_dict[user_id] = user_dict.get(user_id, 0) + 1
    orders_2 = user_dict.get(user_id)
    if orders_2 > max_orders:
        max_orders = orders_2
print(f'Самое большое количество заказов сделал пользователь под номером {user_id}, количество заказов: {max_orders}')

#5
user_dict = {}
max_price = 0
for order_num, orders_data in orders.items():
    user_id = orders_data['user_id']
    user_dict[user_id] = user_dict.get(user_id, 0) + orders_data['price']
    all_price = user_dict.get(user_id)
    if all_price > max_price:
        max_price = all_price
print(f'Пользователь {user_id} имеет самую большую суммарную стоимость заказов за июль: {max_price}')


#6
price_sum = 0
price_count = 0
for order_num, orders_data in orders.items():
    price_sum += orders_data['price']
    price_count = len(orders)
print(f'Средняя стоимость заказа в июле: {price_sum//price_count}')

#7
sum_all, count = 0, 0
for order, data in orders.items():
    sum_all += data['price']
    count += data['quantity']
print(f'Средняя стоимость товаров в июле: {round(sum_all/count)}')