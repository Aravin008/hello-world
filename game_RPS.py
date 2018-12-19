#Game Rock paper scissor 
#User should press r/R for Rock and p/P for Paper and s/S for Scissor
import sys
import os

q=""
ply1=''
ply2=''
msg1="\nCongrats!!"
name1=""
name2=""

def rename():
	global name1,name2
	name1=raw_input("\nEnter player1 name:").capitalize()
	name2=raw_input("\nEnter player2 name:").capitalize()
	print "\nPlayer changed!!"

def display():
	global name1,name2
	print "\n"+ name1+"\'s choice:"+rps(ply1)+"\n"+name2+"\'s choice:"+rps(ply2)


def rps(ch):
	if   ch == 'R':
		return " Rock"
	elif ch == 'S':
		return " Scissor"
	elif ch == 'P':
		return " Paper"
	else: 
		return ch
	

rename()
while(q!="quit"):
	print "\n--------------------------------\n"
	print "----Rock----Paper----Scissor----\n"
	print "--------------------------------\n"
	print "\n "+name1+" should press \nr/R for Rock \np/P for Paper \ns/S for Scissor: "
	ply1=raw_input()
	ply1=ply1[0].capitalize()
	#raw_input("Enter any key")
	print "\n "+name2+" should press \nr/R for Rock \np/P for Paper \ns/S for Scissor: "
	ply2=raw_input()
	ply2=ply2[0].capitalize()
	display()
	#Logic for comparing the player 1 choice with player 2
	if ply1=='R' or ply1 == 'P' or ply1== 'S':
		if ply2=='R' or ply2 == 'P' or ply2== 'S':
			if ply1=='R':
				if ply2 == 'S':
					print msg1+name1+" Wins"
				elif ply2 == 'P':
					print msg1+name2+" Wins"
				else:
					print "\nSorry!! Its a draw Try again"
			elif ply1=='S':
				if ply2 == 'P':
					print msg1+name1+" Wins"
				elif ply2 == 'R':
					print msg1+name2+" Wins"
				else:
					print "\nSorry!! Its a draw Try again"
			elif ply1 == 'P':
				if ply2 == 'R':
					print msg1+name1+" Wins"
				elif ply2 == 'S':
					print msg1+name2+" Wins"
				else:
					print "\nSorry!! Its a draw Try again"
			else:
				print "\n Ohh!! somebody used wrong sign!! Try again"
		else:
			print "\n Ohh!! somebody used wrong sign!! Try again"
	else:
		print "\n Ohh!! somebody used wrong sign!! Try again"
	q=raw_input("\n Type \"quit\" to exit \
			\n Type \"rename\" to change player names \
			\n press any  key to play again:::: ")
	if q == "rename":
		rename()
