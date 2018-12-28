import random

print "----------------------------"
print "--Welcome to Guessing Game--"
print "----------------------------"

def check(n,i_num):
	if (n<i_num):
		print "\nyou guessed high"
	elif (n>i_num):
		print "\nyou guessed low"
	elif (n==i_num):
		print "\ncongrats!! you guessed it right!"
		return 0
	else:
		print "\nyou are crazy!!"
	return 1

n = random.randint(1,9)
i_num=int(raw_input("\nPlease Guess your number:"))
p=1
op_in="start"
while p != 0:
	if(op_in == "quit"):
		break
	else:
		i_num=int(raw_input("\nPlease Guess your number:"))
		p=check(n,i_num)
	op_in=raw_input("\n Type \"quit\" to exit press any key guess again?:")
	

