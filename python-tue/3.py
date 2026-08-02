
age = int(input("please input age:"))
if age >= 18:
   print("you are an adult")

#---------------------------------------

scorepysick = int(input("กรุณากรอกคะแนนฟิสิกส์: "))
scorecall = int(input("กรุณากรอกคะแนนแคล: "))
scoredrowing = int(input("กรุณากรอกคะแนนวิชาวาดภาพ: "))

score = (scorepysick+scorecall+scoredrowing)/3

if score > 95:
   print(score)
   print("congratulation")
else:
   print(score)

#----------------------------------------
num_employees = int(input(" enter the number of employees: "))
print ("this is a small company") if num_employees < 50 else(("this is mediam-sized company") if num_employees < 250 else(("this is a large company") if num_employees >= 250 else("บลาๆๆๆ")))

scores = 75
print("เกรดA") if scores >= 90 else(("เกรด B" )if scores >= 80 else (("เกรดC" )if scores >= 70 else("ไม่มี")))

#----------------------------------------
temperature = 30
if temperature>30:
   print("it's hot ouside.")
elif temperature > 20:
   print("the weather is nice")
else:
   print("it's cold outside")

#-----------------------------------------
inchar = input("input one charater")
if inchar >= "A" and inchar <= "Z":
   print("you in put upper case letter", inchar)
elif inchar >= "a" and inchar <= "z":
   print("you in put lower case letter", inchar)
elif inchar >= "0" and  inchar <= "9":
   print("you in put number ",inchar)
else:
   print("in's not a letter or number", inchar)

#-----------------------------------------
num = float("กรุณากรอกเลขด่วน: ")
if num > 0:
   print("โพซิทีฟนัมเบอร์")
elif num ==  0:
   print("ซีโร่")
else:
   print("เนกกาทีฟ นัมเบอร์")
#-----------------------------------------
scoress = int(input("กรุณากรอกเลข: "))
print("pass or fail message")
if score >= 50:
   print("dissplay \"passs\"")
else:
   print("display \"display fail\"")

#-----------------------------------------
x = 10
y = 20
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#-----------------------------------------
string1 = "mary"
string2 = "mary"

if string1 == string2:
 print(f'"{string1}" and "{string2}" are equa1.')
else:
 print(f'"{string1}" and "{string2}" are not equa1.')

if string1 == string2:
   print(f'"{string1}" come before "{string2}" in lexicographical oder.')
elif string1 > string2:
   print(f'"{string1}" come before "{string2}" in lexicographical oder.')

if string1.lower() == string2.lower():
   print(f'"{string1}" and "{string2}" are equal when case is ignored.')
else:
      print(f'"{string1}" and "{string2}" are equal when case is ignored.')

#-----------------------------------------    
x = 10
y = 20
z = 30

if x < y and y > z:
   print("x is less than y and less than z.")
elif x < y or y > z:
   print("enther x is less than y or y is greater than z.")

if not (x > y):
   print("x is not greater than y.")

#----------------------------------------- 
a = [1,2,3]
b = a

c = [1,2,3]
d = [1,2,3]

print(a is b)
print(a is c)
print(c is d)

print(a == c)
print(c == d)

#----------------------------------------- 

fruits = ["appla","banana","cherry"]

print("banana"in fruits)
print("orange"in fruits)

print("grape" not in fruits)
print("apple" not in fruits)

sentence = "the quick"
print("fox" in sentence)
print("cat" not in sentence)

#-----------------------------------------

age = 25
income = 50000
if age >= 18 and age <= 5 and income > 30000:
 print("you are eligible for the loaan")
else:
   print("you are not eligble for the loan")

#------------------------------------------
nums = float(input("กรอกเลข: "))
if nums > 0:
   print("positive")
elif nums == 0:
   print("zero")
else:
   print("negative") 
#-----------------------------------------
string1 = "mary"
string2 = "mark"

if string1 == string2:
 print(f'"{string1}" and "{string2}" are equa1.')
else:
 print(f'"{string1}" and "{string2}" are not equa1.')

if string1 == string2:
   print(f'"{string1}" come before "{string2}" in lexicographical oder.')
elif string1 > string2:
   print(f'"{string1}" come before "{string2}" in lexicographical oder.')

if string1.lower() == string2.lower():
   print(f'"{string1}" and "{string2}" are equal when case is ignored.')
else:
      print(f'"{string1}" and "{string2}" are equal when case is ignored.')
#----------------------------
# รับค่าชั่วโมงทำงานและอัตราค่าจ้าง
hours = float(input("Enter the number of hours worked: "))
rate = float(input("Enter the hourly pay rate: "))

# คำนวณค่าจ้างตามเงื่อนไข
if hours <= 40:
    # กรณีทำงานไม่เกิน 40 ชั่วโมง
    gross_pay = hours * rate
else:
    # กรณีทำงานเกิน 40 ชั่วโมง (คิดโอที 1.5 เท่าเฉพาะชั่วโมงที่เกิน)
    regular_pay = 40 * rate
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)
    gross_pay = regular_pay + overtime_pay

# แสดงผลลัพธ์ในรูปแบบทศนิยม 2 ตำแหน่ง พร้อมเครื่องหมายจุลภาคคั่นหลักพัน (ถ้ามี)
print(f"The gross pay is ${gross_pay:,.2f}.")

#-------------------------------------------

# 1. แสดงเมนู
print("Please select operation -")
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

# 2. รับค่าจากผู้ใช้ (แปลงเป็น int เพื่อให้เลขออกมาไม่มีทศนิยมตามโจทย์)
choice = input("Select operations form 1, 2, 3, 4 : ")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

# 3. เช็คเงื่อนไขแล้วคำนวณตามตัวเลือก
if choice == '1':
    print(f"{num1} + {num2} = {num1 + num2}")
elif choice == '2':
    print(f"{num1} - {num2} = {num1 - num2}")
elif choice == '3':
    print(f"{num1} * {num2} = {num1 * num2}")
elif choice == '4':
    print(f"{num1} / {num2} = {num1 / num2}")

#*********************************************

#-------------------------------------------