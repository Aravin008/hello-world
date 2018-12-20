#Game Rock paper scissor command based
#User should press r/R for Rock and p/P for Paper and s/S for Scissor
#Yet to add GUI
import sys
import os
#from Tkinter import *

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
	#Read the player choice
	print "\n "+name1+" should press \nr/R for Rock \np/P for Paper \ns/S for Scissor: "
	ply1=raw_input()
	ply1=ply1[0].capitalize()
	print "\n "+name2+" should press \nr/R for Rock \np/P for Paper \ns/S for Scissor: "
	ply2=raw_input()
	ply2=ply2[0].capitalize()
	#display the both player choice
	display()
	#Logic for comparing the player 1 choice with player 2 and announce the result
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

	#This is used for menu at the end of exec, for user to choose
	q=raw_input("\n Type \"quit\" to exit \
			\n Type \"rename\" to change player names \
			\n press any  key to play again:::: ")
	#To rename the players, if not changed the previous names are used
	if q == "rename":
		rename()

#For GUI installed sudo apt-get install python-tk package for Tkinter GUI framawork
import Tkinter as tk
top = tk.Tk()
# Code to add widgets will go here...
top.mainloop()
