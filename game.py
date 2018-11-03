#snake and ladder
import random
count=0

while(count<=100):
	n=input("press r roll the dice")
	if(n=='r'):
		r=random.randint(1,6)	
		count=count+r
		print("u got",r)
		print("new position is",count)
		
		if(count==8):	
			count=37
			print("you got the ladder")
		elif(count==11):
			count=2
			print("sorry, you got the snake")
		elif(count==13):	
			count=34
			print("you got the ladder")
		elif(count==25):
			count=4
			print("sorry, you got the snake")	
		elif(count==38):
			count=9
			
            print("sorry, you got the snake")
        elif(count==40):
        	count=68
        	print("you got the ladder")
        elif(count==52):
        	count=81
        	print("you got the ladder")
        elif(count==65):
        	count=46
        	print("sorry, you got the snake")
        elif(count==76):
        	count=97
        	print("you got the ladder")
        elif(count==93):
        	count=64
        	print("sorry, you got the snake")
        elif(count>=100):
        		print("winner")
                exit()    		