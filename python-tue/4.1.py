for i in range(1,100):
    if i % 2 == 0:
        print(f"{i}นั้นเลขคู่")
    else:
        print([i],"นั้นเลขคี่")

#----------------------------------
num = 0
for i in range(1,11):
    num += i
print(num)
#----------------------------------
num = 0
for i in range(1,11):
    if i % 2 == 0:
        num += i

print(num)
#----------------------------------
total = 0
for i in range(1,21):
    if i % 2 != 0:
            total += 1
print(total)

totol = 5
while totol > 0:
    print(totol)
    totol -= 1
print("boom")
#--------------------------------------------
num = 2
while num > 0:
    for i in range(1,13):
        if i > 0:
            print(f"2x{i} =", num*i)
    break
#--------------------------------------------
        
pp = "python123"
while True:
    number  = input("กรุณาป้อนรหัส: ")
    if number != pp:
        print("รหัสไม่ถูกต้อง กรุณาลองใหม่")
    else:
        print("ยินดีต้อนรับเข้าสู่ระบบ!")
        break
    
#--------------------------------------------
print(("**********\n") * 5, end="")
print(("*******\n") *80)

#--------------------------------------------
#--------------------------------------------

for num in [1,2,3,4]:
    print(num)



l = [1,2,3,4]
for i in l:
    print(i)

for i in range(1,10,2):
    print(i)

for kph in range(60,131,10):
    mph = kph * 0.6214
    print(f"{kph}",f"{mph}")

yes = "y"
while yes == 'y':
    repys = float(input("กรุณากรอกเลข: "))
    repy = repys * 2.5
    print(repy)

print(("**********\n") *5)

score = int(input("enter: "))
while score < 0 or score > 100:
    print("ควย")
    score = int(input("อีกบ่อ: "))

for i in ("ascharporn angthong"):
    if i == "a" or i == "s":
        continue
    print(i)
   
