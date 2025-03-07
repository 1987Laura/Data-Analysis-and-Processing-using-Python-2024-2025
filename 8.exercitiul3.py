
# my_list = ["1", "2", "3", "4"]

# var 1 lambda cu map
print(list(map(str, range(1, 5))))


#var 2 traditional
my_list = list(range(1,5))
print(my_list)

#var 3 List comprehension
my_list = [str(i) for i in range(1,5)]
print(my_list)