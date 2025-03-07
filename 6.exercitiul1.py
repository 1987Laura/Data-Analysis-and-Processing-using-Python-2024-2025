
lista = [10, 2, 30, 50, 300, 10]

#versiunea 1
print(set(filter(lambda x: x > 5, lista)))

#versiunea 2 - list comprehension

print([element for element in lista if element > 5])