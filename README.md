# 🛒 DE_python_final_task - Purchase Analytics Script
**Repository for Task 5 in Data Engineering course**  
**Author:** [Andrei Naideshkin](https://github.com/yourusername)  

---

## 📌 Task Description
As a **Data Engineer**, you need to write a Python script that analyzes store purchase data. The goal is to generate a report with key metrics like revenue, category-wise item distribution, and expensive purchases.

### Input Data
```python
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]
```

### Expected output
```bash
Общая выручка: 21.0  
Товары по категориям: {'fruit': ['apple', 'banana'], 'dairy': ['milk'], 'bakery': ['bread']}  
Покупки дороже 1.0: [
  {'item': 'apple', 'category': 'fruit', 'price': 1.2, 'quantity': 10},
  {'item': 'milk', 'category': 'dairy', 'price': 1.5, 'quantity': 2},
  {'item': 'bread', 'category': 'bakery', 'price': 2.0, 'quantity': 3}
]  
Средняя цена по категориям: {'fruit': 0.85, 'dairy': 1.5, 'bakery': 2.0}  
Категория с наибольшим количеством проданных товаров: fruit

