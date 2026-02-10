#1
nums1 = [1, 2, 3, 4, 5]
square_nums = list(map(lambda n: n * n, nums1))

#2
nums2 = [3, 12, 7, 24, 5, 18, 31, 40]
biger_then10 = list(filter(lambda n: n > 10, nums2))

#3
names = ["dan", "yael", "ori", "noa"]
capital_l = list(map(lambda name: name.capitalize(), names))

#4
words = ["hi", "python", "go", "lambda", "ok", "comprehension"]
len_w_4 = list(filter(lambda word: len(word) >= 4, words))

#5
nums3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_div_by3 = list(filter(lambda n: n % 2 == 0, map(lambda n: n * 3, nums3)))

#6
prices = [100, 200, 50, 80]
discounts = [0.1, 0.2, 0.05, 0.15]
final_price = list(map(lambda price, disc: price * (1-  disc), prices, discounts))

#7
temps_c = [0, 20, 37, 100]
temps_way_a = list(map(lambda t: t * 9/5 + 32, temps_c))
temps_way_b = [t * 9/5 + 32 for t in temps_c]

#8
students = {"Dan": 82, "Yael": 95, "Uri": 67, "Noa": 91, "Shir": 55}
students_way_a = list(map(lambda student: student[0], filter(lambda student: student[1] >= 80, students.items())))
students_way_b = [name for name, score in students.items() if score >= 80]

#9
stock = {"apple": 0, "banana": 12, "cherry": 0, "date": 5, "elderberry": 0}
in_stock_a = {key: val for key, val in stock.items() if val > 0}
in_stock_b = dict(filter(lambda product: product[1] > 0, stock.items()))

#10
products = [
 {"name": "shirt", "price": 100},
 {"name": "pants", "price": 200},
 {"name": "hat", "price": 50}
]
updated_products = list(map(lambda product: {**product, "price_with_vat": product["price"] * 1.17}, products))

#11
employees = [
 {"name": "Dan", "salary": 8000},
 {"name": "Yael", "salary": 15000},
 {"name": "Uri", "salary": 6000},
 {"name": "Noa", "salary": 12000},
 {"name": "Shir", "salary": 9500}
]
filter_emp = list(sorted(map(lambda emp: emp["name"], filter(lambda emp: emp["salary"] > 7000, employees))))

#12
text = " Hello World Python Lambda "
filter_text = list((map(lambda word: word.lower(), filter(lambda word: word != "", text.split(" ")))))

#13
students = [
 {"name": "Dan", "grades": [80, 90, 70]},
 {"name": "Yael", "grades": [95, 88, 92]},
 {"name": "Uri", "grades": [60, 72, 68]}
]
averages = {students["name"]: round(sum(students["grades"]) / len(list(
    map(int, students["grades"]))), 2) for students in students}

#14
orders = [
 {"product": "laptop", "qty": 2, "unit_price": 3000},
 {"product": "mouse", "qty": 10, "unit_price": 50},
 {"product": "screen", "qty": 3, "unit_price": 1200},
 {"product": "keyboard", "qty": 5, "unit_price": 150},
 {"product": "cable", "qty": 20, "unit_price": 30}
]
pipeline_result = sorted(filter(lambda order: order["total"] > 500,map(lambda order: {**order, "total": order["qty"] * order["unit_price"]}, orders)), key=lambda item: item["total"], reverse=True)

#15
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def process_data(data, filter_fn, map_fn):
    return [map_fn(item) for item in data if filter_fn(item)]