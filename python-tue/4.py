print("i will display thr umber i through 5")
for num in[1,2,3,4,5]:
    print(num)

#-----------------------------------------------------

fruits = {"applr","banana","chery"}
for f in fruits:
    print(f)

#-----------------------------------------------------

for char in 'hello':
    print(char)

#-----------------------------------------------------

input_string = input("enter a string: ")
modifind_string = ""
vowels = "aeiouAEIOU"

for char in input_string:
 upper_char = char.upper()

 if upper_char in vowels:
    modifind_string += "*"
 else:
    modifind_string += upper_char
print("modifind string:", modifind_string)

#----------------------------------------------------- เปลี่ยนสระให้เป็น ดอกจัน และเปลี่ยนตัวเล็กเป็นตัวใหญ่

for i in range (5):
 print(i)

print("*"*20,"เพราะแบบนี้ มันจะนับตั้งแต่สูนถึง4เท่านั้นเปรียบเสมือนมี5ตัว")
for i in range (3,10):
 print(i)

print("*"*20,"จะเริ่มตั้งแต่3 เพื่อนับไปเรื่อยๆแต่ไม่แตะ9")
for i in range (1,11,2):
 print(i)

print("*"*20,"เริ่มที่หนึ่ง เดินทีละสอง หยุดที่ 11")

#-----------------------------------------------------

print("number")
print("-"*20)

for number in range(1,11):
  q = number**2
  print(number, "\t", q)

#-----------------------------------------------------

for kph in range(60,131,10):
  mph = kph * 0.6214
  (kph, "\t", mph)

#-----------------------------------------------------
print("-*"*20)
count = 0
while count < 5:
 print("hello:", count)
 count += 1

#-----------------------------------------------------
keep_going = "y"

while keep_going == "y":

    sales = float(input("enter the amount of sales: "))
    comm_rate = float(input("enter the commission rate: "))
    commision = sales * comm_rate

    print(f"the commission in ${commision}")
    keep_going = input("do you want to calculate another")
#-----------------------------------------------------
keep_going = "y"

while keep_going == "y":

    sales = float(input("enter the amount of sales: "))
    sales * 2.5
    comm_rate = float(input("enter the commission rate: "))
    comm_rate * 2.5
    commision = (sales / comm_rate)

    print(f"the commission in ${commision}")
    keep_going = input("do you want to calculate another")

#---------------------------------------------------------

v = int(input("กรุณากรอกเลข:"))
b = int(input("กรุณากรอกเลข:"))

for i in range(v):
    for j in range(b):

        print("*", end="")
print()

#---------------------------------------------------------
import random
print("what is my magic number (1 to 10): ?")
mynumber = random.randint(1,100)
ntries = 1
yourguess = -1
while ntries < 7 and yourguess != mynumber:
   msg = str(ntries) + ">>"
   if (ntries == 6):
      print("your last chance")
   elif (yourguess > mynumber):
      print("--> too high")
   else:
      print("--> too low")
   ntries += 1
if yourguess == mynumber :
   print("yes! it's ", mynumber)
else:
   print("sorry!  my number is", mynumber)
#---------------------------------------------------------

score = int(input("enter a test score: "))
while score < 0 or score > 100:
   print("error: the score cannot be negative")
   print("or great than 100.")
   score = int(input ("enter the correct score"))
#---------------------------------------------------------

for letter in "ascharaporn angthong":
    if letter == "a" or letter == "k":
        continue
    print("curren leter:" , letter)

#--------------------------------------------------------- 

number = [6,5,3,8,4,2,5,4,11]
sum = 0
for val in number:
    sum += val
    print(sum)
print("the sum is", sum)

#---------------------------------------------------------
max = 5
total = 0.0
print("this program calculater the sum of")
print(max,"numbers you will enter.")

for counter in range(max):
   number = int(input("enter a number: "))
   total = total + number
print("the total is", total)

#---------------------------------------------------------

for i in range(1,3):
   for j in range(2,5):
      print(i,j)

#---------------------------------------------------------
for i in range(1,3):
   for j in range(2,5):
      print("i,j")

#---------------------------------------------------------
for i in range(4):
   for j in range(i):
      print("i,j")

#---------------------------------------------------------

for hours in range(24):
   for minutes in range(60):
      for seconde in range(60):
         print(hours, ":", minutes, ":", seconde)
         break
#---------------------------------------------------------
number = int(input("กรุณากอรกเลข: "))
num = int(input("กรุณากอรกเลข: "))
for i in range(number):
   for j in range(num):
      print("*", end="")

#---------------------------------------------------------
print_n = int(input("กรุณากรอก: "))
for i in range(1,101):
   print(f"{i:>3}", end="")
   if i % print == 0:
      print()