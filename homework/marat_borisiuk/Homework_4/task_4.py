my_dict = {'tuple': '', 'list': '', 'dict': '', 'set': ''}
ttuple = (1, 2, 3, 4, 5)
my_dict['tuple'] = ttuple
llist = ['a', 'b', 'c', 'd', 'e']
my_dict['list'] = llist
ddict = {'name1': 'Marat', 'sname2': 'Borisiuk', 'addres': 'SPb', 'age': 38}
my_dict['dict'] = ddict
sset = {False, 1, 2, 38, 'John'}
my_dict['set'] = sset
# print(my_dict)

print(my_dict['tuple'][-1])
my_dict['list'].append(123)
my_dict['list'].pop(1)
my_dict["dict"][("i am a tuple",)] = ("q",)
my_dict['dict'].pop('name1')
my_dict['set'].add('123')
my_dict['set'].remove(38)
print(my_dict)
