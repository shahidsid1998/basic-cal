import fun 
import time
print("-----------------Welcome--------------")
time.sleep(1)
print("Loading 10%....")
time.sleep(1)
print("Loading 30%....")
time.sleep(1)
print("Loading 70%....")
time.sleep(1)
print("Loading Complete :)")
time.sleep(1)
a = int(input("Enter The First Number: "))
b = input("Enter Your Choice: ")
c = int(input("Enter The Second Number: "))

if (b == '+'):
 print("Here Is Your Answer: ",fun.add(a , c))
elif(b == '-'):
 print("Here Is Your Answer: ",fun.sub(a , c))
elif(b == '*'):
 print("Here Is Your Answer: ",fun.mul(a , c))
elif(b == '/'):
 print("Here Is Your Answer: ",fun.div(a , c))
else:
 print("Please Enter Valid Input")
time.sleep(2)
print("---------Basic Calculater By Shahid----------------\n")
time.sleep(1)
print("--------Happy ending--------------")
