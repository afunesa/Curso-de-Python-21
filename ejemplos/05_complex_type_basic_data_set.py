# Sets as known as groups.
# various kind of data (UNIQUE), NOT order and NOT mutable
my_first_set = {'yellow', 'red', 'orange', 'red'}
my_second_set = {'yellow', 'blue', 'pink', 'pink'}
print('set is: ', my_first_set)

# NOT ALLOWED
# my_first_set[1]
# my_first_set[1] = 'blue'
common = my_first_set.intersection(my_second_set)
print('common ', common)

#
minus = my_first_set - my_second_set
print('ONE LESS OTHER', minus)

differnce = my_second_set.difference(my_first_set)
print('differnce is', differnce)

fruits = ['bananas', 'apples', 'pears', 'bananas']
set_fruits = set(fruits)
print('SET FRUITS', set_fruits)