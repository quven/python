#!/usr/bin/env python
x = float(input("enter the value x:"));
n = term  = num = 1;
result = 1.0
while n < 100:
	term *= x/n
  	result += term
  	n+= 1
	#print("term:",term);
  	#print(term< 0.0001);
	if term < 0.0001:
  	  break
print "no of times=",n," and sum = ",result; 	
