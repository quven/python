#!/usr/bin/env python
a = ['shiyanlou','sb','250'];
print(a[::-1]);
print('csb' in a);
print(len(a));
if a :
 print('yes');
else : 
 print('no');
x = [1, 2, 3];
y = ['a', 'b', 'c'];
z = [x, y];
print(z);
print(z[1][1]);
print("===============");
for index in a:
	print(index);

print("-------------");
for index_index in z :
	for index in index_index:
		print(index);

z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
for x in z[::2]:
	print(x);


print(list(range(10)));
print(list(range(5, 10)));


print("**************************");
array = [1, 2, 5, 3, 6, 8, 4];
for i in range(len(array) - 1, 0, -1):
	for j in range(0, i):
		if array[j] < array[j+1]:
			array[j], array[j+1] = array[j+1], array[j];
print(array);		
