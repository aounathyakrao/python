#printing snake and ladder game 
import random 
#
count=0

while(count<=100):
	n=input("press 'r' to roll the dice")
	#start the game
	if(n=='r'):
	#calling random	
		r=random.randint(1,6)
		count=count+r
	#
		print("u got",r)
		print("new position is",count)

		if(count==8):
			count=37
			print(" hey! you got the ladder")
		elif(count==11):
			count=2
			print("su got a snake")
		elif(count==13):
			count=34
			print("hey! you got the ladder")
		elif(count==25):
			count=4
			print("u got a snake")
		elif(count==38):
			count=9
			print("u got a snake")
		elif(count==40):
			count=68
			print("hey! you got the ladder")
		elif(count==52):
			count=81
			print("hey! you got the ladder")
		elif(count==65):
			count=46
			print("u got a snake")
		elif(count==76):
			count=97
			print("hey! you got the ladder")
		elif(count==89):
			count=70
			print("u got a snake")
		elif(count==93):
			count=64
			print("u got a snake")
		elif(count==100):
			print("congragulations!, u won")
			exit()
		elif(count>100):
			print("stay in the same place")
			count=count-r
