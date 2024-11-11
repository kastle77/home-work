def print_parasm(a=1, b='строка' ,c=True):
    print(a, b , c)

print_parasm(b=25)
print_parasm(c=[1,2,3])

values_list = [ 515, 1+ 1j , 0]
values_dict = {'a' : 77 , 'b':True ,'c': 'GG'}

print_parasm(*values_list)
print_parasm(**values_dict)

values_list_2=[54.32 , 'Строка']
print_parasm(*values_list_2,42)