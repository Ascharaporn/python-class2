#ช่องนี้แค่โหมดฝึกเขียน

age = int(input("กรุณากรอกอายุ: "))
if age >= 18:
    print("ว้าวโตแล้วนะเนี่ย")
#------------------------------------------
คะแนนวิชาแรก = int(input("กรุณากรอกคะแนน: "))
คะแนนวิชาที่สอง = int(input("กรุณากรอกคะแนน: "))
คะแนนวิชาที่สาม = int(input("กรุณากรอกคะแนน: "))

all_score = (คะแนนวิชาแรก+คะแนนวิชาที่สอง+คะแนนวิชาที่สาม) / 3

if all_score >= 95:
    print(f"คะแนนของคุณคือ", all_score,"ผ่าน")
else:
    print(f"คะแนนมีแค่",all_score,"ไม่ผ่าน")
#------------------------------------------
number = int(input("กรุณากรอกเลข: "))
if number < 50:
    print("small company")
elif number < 250:
    print("medium company")
elif number >= 250:
    print("larga company")
else:
    print("")
#------------------------------------------

nums = float(input("กรอกเลข: "))
if nums > 0:
   print("positive")
elif nums == 0:
   print("zero")
else:
   print("negative") 
   
#------------------------------------------
x = 10
y = 20
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
#------------------------------------------
while True:
 inchar = input("กรุณากรอกตัวอักษร: ")
 if inchar >= "A" and inchar <= "Z":
    print(f"ตัวหนังสือพิมพ์ใหญ่คือ",inchar)
 if inchar >= "a" and inchar <= "z":
    print(f"ตัวหนังสือตัวเล็กคือ",inchar)
#------------------------------------------
