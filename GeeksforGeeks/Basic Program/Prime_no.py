#Python program to print all Prime numbers in an Interval

n = int(input("Enter the number: "))
for i in range (2,n):
    if n%i==0:
        print(n,"Is not a prime number")
        break
    else:
        print(n,"Prime number")
        break








