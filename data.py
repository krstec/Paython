#list
'''1 list ca store  multiple elements
    2 list can store data of multiple form(like int, str, float)at the same time
    3 list is an ordered collection
    4 list is a mutable data type
    syntsx 
            variabale = [e1, e2, e3, e4------------,en] '''
'''
l = [1, 2, 'Happy Codding ', 45.3, 45]
#type 
print ('the type of l is ', type (l))
#accessing element of list through index values
print(l)
print(l[3])
print(l[-2])
#slicing
print(l[1:5:1])     #end-1
print(len(l))
print('the memeory address/id:of list is : ',id(l))
print ('the index vslus pof each element are ', list(enumerate(l)))
'''


'''
    Q1 
        program to find the length of list
        program to reverse the list using index values
        program to print the 5th element of list using '''