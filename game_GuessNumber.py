import random

print "--------------------------------"
print "--Welcome to Guess Number Game--"
print "--------------------------------"

def check(n,i_num):
	diff=abs(n-i_num)
	#print str(n)+"diff:"+str(diff)		#for debug
	if diff>100:
		if(n<i_num):
			print "\noh.. you guessed crazy far and high"
		else:
			print "\noh.. you guessed crazy far and low"
#	if diff>70:
#		if(n<i_num):
#			print "\noh.. you guessed  high"
#		else:
#			print "\noh.. you guessed crazy low"
	elif diff>50:
		if(n<i_num):
			print "\nyou guessed very high!"
		else:
			print "\nyou guessed very low!"
	elif diff>30:
		if(n>i_num):
			print "\nyou guessed far low"
		else:	
			print "\nyou guessed far high"
	elif diff>=20:
		if(n>i_num):
			print "\nlittle close and low"
		else:	
			print "\nlittle close and high"
	elif diff>5 and diff<20:
		if(n>i_num):
			print "\nyou are very close but low"
		else:	
			print "\nyou are very close but high"
	elif diff<=5 and diff>0:
		print "you are crazy near"
	elif (n==i_num):
		print "\ncongrats!! you guessed it right!"
		return 0
	else: 
		print "\n you have a long way go"
	return 1


#Game block start
print "\nInstructions:\n1) Enter Range Ex: 1 100 (Min:1,Max:1000)\n2)Please type \"0\" any instance to quit the game\n3)Have fun!!"
low,high=map(int, raw_input("\nEnter low, high range:").split())
n = random.randint(low,high)
#print str(n)+"\n"  #for debug
p=1
i_num=1111
while p != 0:
	if(i_num == 0):
		break
	else:
		try:
			i_num=int(raw_input("\nPlease Guess your number:"))
		except:
			i_num=0
			print "\nPlease enter integer value.."
		if i_num !=0:
			p=check(n,i_num)

