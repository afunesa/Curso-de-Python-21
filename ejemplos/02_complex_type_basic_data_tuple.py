# Tuples
# various kind of data, order and NOT mutable
my_first_tuple = (1, 'a string', False, 1, 2, False)
print(my_first_tuple)
print('first element ->>', my_first_tuple[0])
print(my_first_tuple.index(False))
print('count number of falses', my_first_tuple.count(False))
# not allowed
# my_first_tuple[1] = 'change'
my_second_tuple = tuple()
third_tuple = ()