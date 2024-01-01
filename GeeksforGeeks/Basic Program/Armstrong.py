#Python Program to check Armstrong Number.
'''num = int(input("Enter any number: "))
sum = 0
# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")'''

'''num = int(input("Enter the number: "))
sum = 0
temp = num
while temp>0:
   digit = temp % 10
   sum = sum + digit ** 3
   temp //=10
   
#display the result
if num == sum:
   print(num,"It is true")
else:
   print(num,"Ti is false")'''

#We have to find out Armstrong

num = int(input("Enter the number: "))
sum = 0
restore = num
while restore>0:
   total = restore%10
   sum = sum + total**3
   restore//=10

if num == sum:
   print(num, "Yes")
else:
   print(num, "No")































