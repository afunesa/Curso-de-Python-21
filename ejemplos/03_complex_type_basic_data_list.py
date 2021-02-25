# complex data, lists
# various kind of data, order and mutable

my_empty_list = []
other_way_empty_list = list()

buying_list = ['bananas', 'apples', 1]
#                   0   ,    1    , 2
#                -3    ,     -2   , -1
print('original buying list ', buying_list)
print('first value', buying_list[0])
print('third value', buying_list[2])
buying_list[0] = 'pears'
print('first element has changed to', buying_list[0])
print('full list has changed to', buying_list)
print('length of buying_list', len(buying_list))

buying_list.append('chocolate')
print('list has changed to', buying_list)
extracted = buying_list.pop()
print('list has changeg to', buying_list)
print('we have deleted ', extracted)
buying_list.remove('apples')
print('DELETED WAS', buying_list)
buying_list.append('cookies')
print('#######################')
second_list = ['bananas', 'apples', 1]
print(second_list)
splitted_list = second_list[0:2]
second_splitted = second_list[:1]
third_back = second_list[:-2]
print('splitted_list', splitted_list)
print('second_splitted', second_splitted)
print('third_back', third_back)

## CHANGE LIST DIRECTLY WITH INDEX
second_list[0] = 'other thing'
print('MODIFIED!!', second_list)




####

a_character = 'a'
another_character = 'b'
together = a_character + another_character