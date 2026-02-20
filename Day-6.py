#find sum of even numbers upto n
n =int(input())
i= 0
total = 0
while(i<n+1):
    total+=i
    i+=2
print(total)

#print 1-100 numbers
i= 0
while(i<101):
    print(i,end=" ")
    i+=1

#print even numbers between 10 -40
n,m=map(int,input().split())
total = 0
if(n%2!=0):
    n+=1
while(n<m+1):
    total+=n
    n+=2
print(total)    
    
#finding the length of the number
n=int(input())
count = 0
while(n>0):
    n=n//10
    count+=1
print(count)



#finding the sum of digits
n = int(input())
sum1 =0
while(n>0):
    sum1+=n%10
    n//=10
print(sum1)


# reverse The number without using the strings

n = int(input())
rev = 0
while(n>0):
    rem = n%10
    rev=rev*10+rem
    n//=10
print(rev)


#wether the number is amstrong or not
n =int(input())
length =len(n)
while(n>0):
    



#perfect number
n= int(input())
i =1
res=0
while(i<=n//2):
    if(n%i==0):
        res=res+i
    i+=1
if(n==res):
    print("Perfect number")
else:
    print("not a perfect number")















