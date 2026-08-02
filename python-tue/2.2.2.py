first = int(input("กรุณากรอกชื่อตัวเอง: "))
firstname = str(first)
lastname = input("กรุณากรอกชื่อตนเอง: ") 
print("hay!" + firstname,lastname)

หมอน = 45
หมอน2 = float(หมอน)+10
print("หมอนใบแรกมีราคา%d และหมอนใบที่สองมีราคาอยู่ที่%.2f" %(หมอน,หมอน2))

income = float(input("กรุณากรอกเงินฝาก: "))
print("income: ",format(income,"12,.2f"))

ff  = 15
dd = 44
print(ff + dd , str(ff) + str(dd))

ชื่อผลไม้ = ["แอปเปิ้ล", "กล้วย", "ส้ม"]
ราคา = [50, 40, 80]
ผลลัพ = zip(ชื่อผลไม้,ราคา)
print(list(ผลลัพ))


#-----------------------------------------------------------------------------------------------------


#for ไม่สามารถใช้ตั้งชื่อได้
class customerAccount:
    def __init__(self, name , balance):
        self.name = name
        self.balance = balance

com = 3+4j
#-----------------
a=b=c=d=e =0.0

dd = 25
ddd = float(dd)
print('หมอนแรกมีน้ำหนัก%d หมอนสองมีน้ำหนัก %.2f' %(dd,ddd))

x = 15
y = 4

print('15+4 =', x+y)
print("15-4 =", x-y)
print("15x4 =", x*y)
print("15/4 =", x/y)
print("15%4 =", x%y )
print("15//4 =",x//y)
print("15**4 = ", x**y)

name = input("กรุณากรอกชื่อ: ")
namm = input("กรุณากรอกนามสกุล: ")
print("hay!" + name,namm)

number = input("กรุณากรอกเลข: ")
result = int(number) + 10
print(result)

result = int(number) + 5
print(result)


#------------------------ทดลอง
nn = input("กรอกเลข: ")
mm = int(nn) + 45
print(mm)

gg = 45
hh = float(gg)
print("%d %f"%(gg,hh))
#------------------------หยุดทอลอง


income = float(input("กรุณากรอกเงินฝาก: "))
print("income: ",format(income,"12,.2f"))


#------------------------ทดลอง

print("income: ", format(income,"12,.2f"))
print("income: ", format(income,"12,.2f"))
print("income: ", format(income,"12,.2f"))
print("income: ", format(income,"12,.2f"))
print("income: ", format(income,"12,.2f"))
print("income: ", format(income,"12,.2f"))

ผลลัพ = zip(ชื่อผลไม้,ราคา)
print(list(ผลลัพ))

print("income: ", format(income,"12,.2f"))
ผลลัพ = zip(ชื่อผลไม้,ราคา)
print(list(ผลลัพ))

#------------------------หยดทดลอง

age = input("กรุณากรอกอายุ: ")
ages = int(age)

height = input("กรุณากรอกความสูง: ")
heights = float(height)
print("อายุคุณคือ", str(ages), "ความสูงคือ" + str(heights))

weight = int(input("กรุณากรอกน้ำหนัก: "))
heightss = int(input("กรุณากรอกส่วนสูง: "))
bmi = weight / (heightss*heightss)
print(bmi)

celsius = int(input("กี่องศาเซลเซียส: "))
fahrenheit = (celsius*9/5 + 32)
print(fahrenheit)

