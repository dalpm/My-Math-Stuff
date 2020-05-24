import math
import operator
import sys
try:
    x = int(input("Asal çarpanlarını öğrenmeyi istediğiniz sayıyı giriniz: "))
except ValueError or NameError:
    print("error")
    sys.exit(1)
while x <= 1:
    print ("Sayının 1'den büyük olması gerekir: ")
    break
y = 1
prime_dividers = []
#School method is_prime
#Primality test
def is_prime(y): 
    if y <= 1: 
        return False
    else:
    # Test the divider with the numbers from 2 to
    #the number itself to decide if the number is prime or not.
        if y > 3:
            # If the divider is different from 2 and 3 but can be divided by 2 or 3, it returns false
            # and calculation gets faster. 
            if y % 2 == 0 or y % 3 == 0:
                return False 
            else:
                for i in range(2, y): 
                    if y % i == 0: 
                        return False
    return True
while y < x:
    y = y+1 
    if x % y == 0:
        if is_prime(y) == True:
            prime_dividers.append(y)
print(str(x) + " sayısının asal çarpanlar kümesi = " + str(prime_dividers))