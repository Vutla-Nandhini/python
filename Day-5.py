num1 =int(input())
num2 = int(input())
num3 = int(input())
if num1 >=num2 and num1>=num3:
    print("The bigger number is",num1)
elif num2>=num3:
    print("The bigger number is",num2)
else:
    print("The bigger number is",num3)

a,b,c = map(int,input().split())
if(a%2 == 0):
    print("The number is even")
else:
    print("The number is odd")
if(b%2 == 0):
    print("The number is even")
else:
    print("The number is odd")
if(c%2 == 0):
    print("The number is even")
else:
    print("The number is odd") 


lst =[11,12,13,14,15]
for i in range(0,5,1):
    if(lst[i]%2 == 0):
        print(lst[i],"is Even")
    else:
        print(lst[i],"is Odd") 

#print even numbers between 20-40
for i in range(20,41,2):
    print(i)

for i in range(20,41):
    if(i%2==0):
        print(i) """

for i in range(1,101):
    print(i,sep="",end=" ") 

num = int(input())
total = 0
for i in range(1,num+1):
    total +=i
print(total)    
    





