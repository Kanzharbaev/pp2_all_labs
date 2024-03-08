from math import prod
def multiply(numbers):
    return prod(numbers)
my_lis=[int(i) for i in input().split()]
result=multiply(my_list)
print(result)   #ex1

def count(string):
    lower_count=0
    upper_count=0
    for i in string:
        if i.islower():
            lower_count+=1
        elif:
            i.isupper():
            upper_count+=1
    return lower_count, upper_count

string=input()
lower,upper=count(string)
print(f"Number of uppercase letters: {upper}")
print(f"Number of lowercase letters: {lower}")   #ex2

def is_palindrom(string):
    string2=string[::-1]
    if string=string2:
        return("The string is a plaindrome")
    else:
        return("The string is not a palindrome")

string=input()
print(is_palindrom(string))  #ex3

import time
number=int(input("Enter a number to find its sqare root: "))
delay=int(input("Enter the number of milliseconds to delay"))
delay_sec=delay/1000
sleep(delay_sec)
sqrtnumber=pow(number, 0.5)
print(f"Square root of {number} after {delay} milliseconds is {sqrtnumber}")   #ex4


def all_true(tuple):
    return all(tuple)

tuple_1=[True, True, False]
print(all_true(tuple_1))
tuple_2[True, True, True]
print(all_true(tuple_2))    #ex 5



            

