#This file is test file
print("\n\n python program\n")
#a=10
#b=12
#print "\n Addition=",a+b 
#name = raw_input("What's your name? ")
#print("Nice to meet you " + name + "!")
#age = raw_input("Your age? ")
#print("So, you are already " + str(age + 10) + " years old, " + name + "!")

#List within n value
a=[1,12,2,49,85,78,3,22,55,63]
b=[]
print "Enter the n val:"
n=int(raw_input())
for element in a:
	if element<n:
		b.append(element)
print "Elements in list a:",a
print "Elements in list b:",b
