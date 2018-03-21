#!/usr/bin/env python
sticks = 21;
print("you will choose (1-4) sticks");
print("whoever will take the last stick will loose");
while True:
	print "sticks left:",sticks;
	sticks_taken = int(input("take sticks (1~4):"));
	if sticks == 1:
		print("you loose");
		break;
	if sticks_taken <= 0 or sticks_taken >= 5:
		print("wrong choice");
		continue;
	print "computer took:", (5-sticks_taken);
	sticks -= 5;
