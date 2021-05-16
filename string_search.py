# 22.08.2020 Алгоритм поиска символов 2-строки в первой. Либо поиск символов которых нет в первой строке.

a_string = "hello"
b_string = 'health'
c_1 = []
d_1 = []

a_1 = [i for i in a]
print(a_1)
b_1 = [(lambda fin: a_1.count(i))(i) for i in b]  # Колл-во символов 2 строки в первой.
print(b_1)

for i in a:
	c_1.append(i)
print(c_1)
for i in b:
	if not c_1.count(i):
		d_1.append(i)
print(d_1)