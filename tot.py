a=['1','2','3','4','5','6','7','8','9']

def print_board():
	print(a[0],'|',a[1],'|',a[2])
	print("------------")
	print(a[3],'|',a[4],'|',a[5])
	print("------------")
	print(a[6],'|',a[7],'|',a[8])

riya turn = True
while True:
		print_board()
		p=input("choose an available place:")

		if(p is a):
			if (a[int(p)1]=='x'or a[int(p)-1]=='0'):
				pirnt("place taken , choose another place...")
				countinue
			else:
				if riya turn:
					print("player 1>>")
					a[int(p)-1]
					riya turn= not riya turn
			    else:
			    	print("player 2>> ")
			    	a[int(p)-1]='0'
			    	riya turn= not riya turn
			for i in(0,3,6):
				if(a(i))

			


