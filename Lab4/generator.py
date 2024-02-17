n=int(input())
square_num=(i**2 for i in range(1,n+1))
print(*square_num)  #ex1

num=int(input())
even=(i for i in range(n+1) if i%2==0)
print(*even,sep=",")   #ex 2

number=int(input())
div=(i for i in range(number) if(i%3==0 and i%4==0))
print(*div,sep=" ")  #ex3

def squares(a,b):
    for i in range(a,b+1):
        yield i**2

a=int(input())
b=int(input())
print(*squares(a,b))   #ex4

number=int(input())
print(*(i for i in range(n,-1,-1)))   #ex5


