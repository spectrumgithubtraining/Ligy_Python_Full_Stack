# list1 = [1, 2, 3, 4]
# list2 = ['a', 'b', 'c', 'd']
# print(zip(list1, list2))


list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

# Iterate over two lists simultaneously using zip
for item1, item2 in zip(list1, list2):
    print(item1, item2)