"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

#Check if number is prime
list1 = []
for num in range(2,150000):
    if all(num%i!=0 for i in range(2,num)):
        list1.append(num)
print (list1[10000])
