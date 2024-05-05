# x = 42
# y = x

# print(id(x))
# print(id(y))
# y += 1
# some_variable = True

# print(some_variable is True)

# my_dict = {"x": 1, "y": 2}
# another_dict = my_dict.copy()

# another_dict["x"] = 100

# print(my_dict)
# print(another_dict)
# another_dict["x"]

lst = [2, 3, 4]

another_list = [i ** 2 for i in lst]

lst.extend(another_list)

print(lst)
