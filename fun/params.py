#!/usr/bin/env python

def power(x, n = 2):
	s = 1
	while n > 0:
		s = s * x
		n -= 1
	print(s)
power(4, 4)


def enroll(name, gender ,city = 'beijing', age = 28):
	print "name=",name;
	print "gender=",gender;
	print "city=",city;
	print "age=",age;
enroll('xuehao','S',age= 7)

# check in php
def add_end(L=[]):
	L.append('END')
	print(L)
#add_end();
#add_end();
#add_end();
def add_end_power(L = None):
	if L is None:
		L = []
	L.append('End')
	print(L)
add_end_power()
add_end_power()
add_end_power()

def calc(numbers):
	sum = 0;
	for i in numbers:
		sum += i*i
	print(sum)
def calc_variable(*numbers):
	sum = 0;
	for i in numbers:
		sum += i*i
	print(sum)
calc([1, 3, 5])
calc_variable(1,2,3)
num = [1,2,3]
calc_variable(num[0], num[1], num[2])
print("-------------------------");
calc_variable(*num)

def person(name, age, **kw):
	print "name:",name,"age:",age,"other:",kw
person('xuehao', 28, city='beijing',job='eng')
extra = {'city':'beijing','job':'enginer'}
person('xuehao', 21, city=extra['city'], job=extra['job'])

person('xuehao',22, **extra)
