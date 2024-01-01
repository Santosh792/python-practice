#Python program to check whether a number is Prime or not

n = int(input("Enter the number: "))
for i in range (2,n):
    if n%i==0:
        print(n,"Is not a prime number")
        break
    else:
        print(n,"Prime number")
        break








