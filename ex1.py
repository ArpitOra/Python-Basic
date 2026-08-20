'''Learnig How To Input And Output Data In Python


print("Welcome to the Python script!")
First_Name = input("Please enter your first name: ")
Last_Name = input("Please enter your last name: ")
Age = int(input("Please enter your age: "))
Height = int(input("Please enter your height in centimeters: "))

import time
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")

print ("Hello, " , First_Name , "", Last_Name , "! Nice to meet you.")
print("Your Age After One Year will Be", Age+1,type(Age), "years old and your height is", Height, "cm.")
print("Thank you for using the Python script. Have a great day!")  



import time
print("Welcome to the Python script!")
time.sleep(3)
First_Name = input("Please enter your first name: ") 
time.sleep(3)
print("I Am Taking Your First Name As Input...")
time.sleep(3)
print("Your First Name is Successfully Entered Which is: ", First_Name)
'''

R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
BO = "\033[1m"
RE = "\033[0m"

print(f"{R}WARNING: This script is for educational purposes only. Please use it responsibly.{RE}")