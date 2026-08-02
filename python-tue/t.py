string1 = "mary"
string2 = "mark"

# 1. เช็กความเท่ากัน
if string1 == string2:
    print(f'"{string1}" and "{string2}" are equal.')
else:
    print(f'"{string1}" and "{string2}" are not equal.')

# 2. เช็กการเรียงลำดับตามพจนานุกรม
if string1 < string2:
    print(f'"{string1}" comes before "{string2}" in lexicographical order.')
elif string1 > string2:
    print(f'"{string2}" comes before "{string1}" in lexicographical order.')
else:
    print(f'"{string1}" and "{string2}" are identical.')

# 3. เช็กความเท่ากันโดยไม่สนใจพิมพ์เล็ก-พิมพ์ใหญ่
if string1.lower() == string2.lower():
    print(f'"{string1}" and "{string2}" are equal when case is ignored.')
else:
    print(f'"{string1}" and "{string2}" are NOT equal even when case is ignored.')
#------------------------------
x = 10
y = 20
z = 30

if x < y and y > z:
   print("x is less than y and less than z.")
elif x < y or y > z:
   print("enther x is less than y or y is greater than z.")

if not (x > y):
   print("x is not greater than y.")
#------------------------------
x = 5
y = 10
z = 15
if x < y and y < z:
    print("yes")
if x < y or y > z:
    print("yes")
if not x > y:
    print("yes")
#----------------------------
x = "hello"
y = "hello"  # (สำหรับ String สั้น ๆ ใน Python บางทีมันจะแชร์ตำแหน่งเดียวกัน)

# แต่ถ้าเป็นพวกข้อมูลกลุ่ม (List)
list1 = [1, 2]
list2 = [1, 2] 

print(list1 == list2) # True -> เพราะหน้าเหมือนกัน (ข้างในมี 1, 2 เหมือนกัน)
print(list1 is list2)  # False -> เพราะเป็นกล่องคนละใบที่สร้างขึ้นมาแยกกัน

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