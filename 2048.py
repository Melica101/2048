import random
def listShift(list1):
	list2=[]
	for i in list1:
		if i!=0:
			list2.append(i)
	for a in range(len(list1)-len(list2)):
		list2.append(0)
	return list2
def listMerge(lst):
        listA=listShift(lst)
        i=1
        for i in range(1,len(listA)):
                if listA[i]==listA[i-1] and listA[i] != 0:
                        listA[i-1]=listA[i-1]+listA[i]
                        listA[i]=0
        listR=listShift(listA)
        return listR
def transpose(lst2):
        newlist=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for i in range (4):
                for j in range(4,0,-1):
                        k=j-1
                        newlist[i][k]=lst2[k][i]
        return newlist


list2d=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range (2):
        x=random.randint(0,5)
        if 0<=x<5:
                list2d[random.randint(0,3)][random.randint(0,3)]=2
        else:
                list2d[random.randint(0,3)][random.randint(0,3)]=4

def game():
        global list2d
        ans2=input("In which direction would you like the numbers to add?")
        if ans2=='a' or ans2=='A'  or ans2=='4': #to go left
                for h in range(len(list2d)):
                        list2d[h]=listMerge(list2d[h])
                i=random.randint(0,3)
                j=random.randint(0,3)
                if list2d[i][j]==0:
                        list2d[i][j]=2  #to keep the game going
                for x in list2d:
                        print(x)
                print("---------------------------------------------------------")
        elif ans2=='d' or ans2=='D' or ans2=='6': #to go right
                for i in list2d:
                        i.reverse()
                for h in range(len(list2d)):
                        list2d[h]=listMerge(list2d[h])
                i=random.randint(0,3)
                j=random.randint(0,3)
                if list2d[i][j]==0:
                        list2d[i][j]=2  #to keep the game going
                for x in list2d:
                        x.reverse()
                        print(x)
                print("---------------------------------------------------------")
        elif ans2=='w' or ans2=='W' or ans2=='8': #to go up
                list_transpose=transpose(list2d)
                for h in range(len(list_transpose)):
                        list_transpose[h]=listMerge(list_transpose[h])
                list2d=transpose(list_transpose)
                i=random.randint(0,3)
                j=random.randint(0,3)
                if list2d[i][j]==0:
                        list2d[i][j]=2  #to keep the game going
                for x in list2d:
                        print(x)
                print("-------------------------------------------------------------")
        elif ans2=='z' or ans2=='Z' or ans2=='2': #to go down
                list2d.reverse()
                list_transpose=transpose(list2d)
                for h in range(len(list_transpose)):
                        list_transpose[h]=listMerge(list_transpose[h])
                list2d=transpose(list_transpose)
                list2d.reverse()
                i=random.randint(0,3)
                j=random.randint(0,3)
                if list2d[i][j]==0:
                        list2d[i][j]=2  #to keep the game going
                for x in list2d:
                        print(x)
                print("---------------------------------------------------------------")
        else:
                print("INVALID INPUT!!!")
        for x in list2d:
                if min(x)==0:
                        pass
                else:
                        print("GAME OVER!!!")
                        return 1

        
print("***********************************************", "welcome to the game 2048","************************************************************************************************************************************************************")
print("-----------------------------------------------------------------" *2)
print("\t\t\t","The rules are simple,\nTo add two equal consecutive numbers type the diretion\n to add them in")
print("\t\t To go up use either 'w' or '8' \n  \t\t To go down use either 'z' or '2' \n \t\t To go to the left use either 'D' or '6' \n\t\t To go to the right use either 'A' or '4' \n")
ans= input("\t\t to get started enter Y ")
if ans=='Y' or ans=='y':     #so it works for both capital and small
        for x in list2d:
                print(x)
                        
while ans=='y' or ans=='Y':
        game()
        
        

	
			
		
				
			
				
	
			
			
	
		
			
		
