'''st = input('Enter the name')
#count of the total charcter
print(f'the leanth of user string is {len(st)}')
#count of user cahrctor
ch = input('Enter the any character to count')
print('the count of {} is: {}'.format(ch,st))
#replace  user defined charcter
ch_to_rep=input ('Enter the charcter to replace from string: ')
ch_with = input('Enter the charcter with to replace: ')
print('the string after replacing the character is: %st' %(s.replace(ch_to_rep,ch_with)))
'''
'''#Q2
s=input('enter the string:- ')
char= input('Enter any charcter to place around the string: ')
print ('the string after center method is:' st.center(len(s)+10,char))'''
'''# 17/01/22
#dir(list)
#index()
l = [1,2,3,56.34, 'happy codding', 'paython','good']
print(l)
print(l.index('good'))
l=l.copy()
print(l)
l2=[]
l2.append(45)
l2.append('kra8tec')
l2.append('krs')
print(l2)
#extend
l2.extend([1,2,3,4])
print(l2)
#remove
#pop
print(l2)
#single
l2.pop
print(l2)
l2.pop(3)
print(l2)
#remove
l2.remove(2)
print(l2)
#insert
l2.insert(0,'pyhton')
print(l2)
l2.reverse()
print(l2)
#shorting
#short
l3=[1,2,45,33]
l3.sort()
print(l3)
#reverse
l3.reverse()
print(l3)
#clear
l2.clear()

print(l2)
#del()
del(l2)
#print(l2)'''
'''#user dfine list 
l4 = input('Enter a list').split()
print(l4)
print(type(l4))'''
'''
    program to take a user defined list and then add  element of user defined choice to list using single multiple syntax
    program to remove user defined value
    progaram to sort a list of string type
    
    program to element to list without inbuilt method
    program in update element
    program remove element iny list inbult method

    
'''
l5 = input('Enter a list:- ').split()
print(l5)
a=input('Enter the one list:-')
l5.append(a)
print(l5)
b= input('Enter the multiple list:-').split()
l5.extend(b)
print(l5)
c = input('you are remove any value, then write value name:-')
print('are you sure remove this value:',c)
l5.remove(c)
print(l5)
l5.sort()
print(l5)











