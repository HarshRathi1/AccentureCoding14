'''Write a program in C such that it takes a lower limit and upper limit as inputs and print all the intermediate palindrome numbers.

Test Cases:

TestCase 1:
Input :
10 , 80
Expected Result:
11 , 22 , 33 , 44 , 55 , 66 , 77.'''
l=[]
n1,n2=map(int,input().split())
for i in range(n1,n2+1):
    rev=0
    temp=i
    while temp>0:
        r=temp%10
        rev=rev*10+r
        temp=temp//10
    if i==rev:
        l.append(i)
print(*l,sep=',')
'''Another Solution
for i in range(10,99):
    a=str(i)[::-1]
    if i==int(a):
        print(i)'''
