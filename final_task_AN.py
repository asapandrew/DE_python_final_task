from purchases_data import purchases

def total_revenue(purchases):
    sum = 0
    for purchase in purchases:
        amount = purchase["price"] * purchase["quantity"]
        sum += amount

    return sum


def items_by_category(purchases):
    cat_item = {}
    for purchase in purchases:
        if purchase["category"] not in cat_item:
            cat_item[purchase["category"]] = []
        if purchase["item"] not in cat_item[purchase["category"]]:
            cat_item[purchase["category"]].append(purchase["item"]) 

    return cat_item


def expensive_purchases(purchases, min_price):
    min_price = 1.0
    list = []
    for purchase in purchases:
        if purchase["price"] > min_price:
            list.append(purchase)    

    return list


def average_price_by_category(purchases):
    cat_item = items_by_category(purchases) # {'fruit': ['apple', 'banana'], 'dairy': ['milk'], 'bakery': ['bread']}
    item_price = {} # {'apple': 1.2, 'banana': 0.5, 'milk': 1.5, 'bread': 2.0}
    avg_price = {}

    for purchase in purchases:
        item_price[purchase["item"]] = purchase["price"]

    for category in cat_item: # category = 'fruit'
        total_price = 0
        for item in cat_item[category]: # item = 'apple'     #cat_item[category] # ['apple', 'banana']
            price = item_price[item]
            total_price += price
        
        num_of_items = len(cat_item[category])
        avg_price[category] = total_price / num_of_items

    return avg_price


def most_frequent_category(purchases):
    cat_item = items_by_category(purchases) # {'fruit': ['apple', 'banana'], 'dairy': ['milk'], 'bakery': ['bread']}
    item_cnt = {} # {'apple': 10, 'banana': 5, 'milk': 2, 'bread': 3}
    frequency = {}

    for purchase in purchases:
        item_cnt[purchase["item"]] = purchase["quantity"]

    for category in cat_item: # category = 'fruit'
        total_cnt = 0
        for item in cat_item[category]: # item = 'apple'     #cat_item[category] # ['apple', 'banana']
            cnt = item_cnt[item]
            total_cnt += cnt
        
        frequency[category] = total_cnt
    
    category_with_max_value = max(frequency, key=frequency.get)
    
    return category_with_max_value


min_price = 1.0

print(f"Общая выручка: {total_revenue(purchases)}")
print(f"Товары по категориям: {items_by_category(purchases)}")
print(f"Покупки дороже {min_price}: {expensive_purchases(purchases, min_price)}")
print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
print(f"Категория c наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")