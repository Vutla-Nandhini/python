# weather the given input is correct  password or not
n = input()
ori = input()
if(n == ori):
    print("correct Password")
else:
    print("wrong Password") 


# Is the person eligible for vote or not
age =int(input())
if(18<= age ):
    print("eligible for vote")
else:
    print("Not eligible for vote") 


#the number is negative,positive,zero
n = int(input())
if(n<0):
    print("Negative")
elif(n>0):
    print("Positive")
else:
    print("Zreo") 


#Among three numbers which number is greater
a,b,c = map(int,input().split())
if(a == b == c):
    print("greater number is",a)
elif(a>b and a>c):
    print("greater number is",a)
elif(b>c):
    print("greater number is",b)
else:
    print("greater number is ",c)



# checking citizen + age eligible for vote
age = int(input())
citizen = input()
if(age>=18):
    if(citizen == "citizen"):
        print("Eligible for voting")
    else:
        print("Not Eligible for voting") 


 #using nested if       
a,b,c,d =map(int,input().split())
if(a>b and a>c):
    if(a>d):
        print("a is greater")
elif(b>c and b>d):
    print("b is greater")
elif(c>d):
    print("c is greater")
else:
    print("d is greater") """































    
    
