#Game Rock paper scissor command based
#User should press r/R for Rock and p/P for Paper and s/S for Scissor
#Yet to add GUI
import sys
import os
#from Tkinter import *
import getpass 
  

q=""
ply1=''
ply2=''
msg1="\nCongrats!!"
name1=""
name2=""
Hide=0

def Hide():
	global Hide
	hch = raw_input("\n Do you want to hide info (y/n)??")[0].capitalize()
	if hch =='Y':
		Hide=1;
	elif hch == 'N':
		Hide=0;
	else:
		print "\n Retry press (y/n)"
		Hide()
	
def rename():
	global name1, name2
	name1 = raw_input("\nEnter player1 name:").capitalize()
	name2 = raw_input("\nEnter player2 name:").capitalize()
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
	
#"""

Hide()			# Option to display/hide the info
rename()		# Option to Name/Rename players
while(q!="quit"):
	print "\n--------------------------------\n"
	print "----Rock----Paper----Scissor----\n"
	print "--------------------------------\n"

	#Read the player choice and capitalize the chatacter
	print "\n"+name1;
	if Hide == 0:
		print "Press \nr/R for Rock \np/P for Paper \ns/S for Scissor "
	try: 
    		ply1 = getpass.getpass(prompt='Your Choice:  ')
	except Exception as error: 
    		print('ERROR', error) 
	else: 
	    	print "" 
	ply1=ply1[0].capitalize()
	print "\n"+name2;
	if Hide ==0:
		print "Press \nr/R for Rock \np/P for Paper \ns/S for Scissor: "
#	ply2=raw_input()
	try: 
    		ply2 = getpass.getpass(prompt='Your choice: ')
	except Exception as error: 
    		print('ERROR', error) 
	else: 
	    	print "" 
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
			\n Type \"hide\" to hide the info \
			\n press any  key to play again:::: ")
	#To rename the players, if not changed the previous names are used
	if q == "rename":
		rename()
	if q == 'hide':
		Hide()
"""
#For GUI installed sudo apt-get install python-tk package for Tkinter GUI framawork
import Tkinter as tk
root = tk.Tk()
w=tk.Label(root,text="Stone_Paper_Scissor",  fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic")
w.grid(row=0,column=0,columnspan=9)
player1_Img=tk.PhotoImage(file="house_1.ppm")
player2_Img=tk.PhotoImage(file="west_1.ppm")
ply1Img =tk.Label(root,image=player1_Img).grid(row=1,column=1)
ply2Img = tk.Label(root, image=player2_Img).grid(row=1,column=6)

winner=tk.Label(root,text="WINNER")
winner.grid(row=6,column=5,columnspan=3)
# Code to add widgets will go here...
root.mainloop()
"""
