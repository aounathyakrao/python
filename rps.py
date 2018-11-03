import random
a=['r','p','s']
s1=0
s2=0
while (true):
		p=input("your choice r/p/s: ")
		c=random.choice(a)

		print("you chose",p,"computer chose",c )
		if(p=='r' or p=='p' or p=='s'):
			elif(p==c):
				print("tie")
		elif((p=='r' and c=='p') or (p=='p' amd c=='s') or (p=='s' and c=='r')):
			s1=s1-1
			print("computer won",s2, "times")
		else:
			s2=s2+1
			print("u won",s2,"times")