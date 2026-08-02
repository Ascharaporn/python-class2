def main_day(pay):
  return "bra bra bra " if pay > 10 else ("no bra bra bra" if pay == 10 else "no")
while True:
   your = int(input("กรุณากรอก เงินของคุณ: "))
   buys = main_day(your)
   if your >= 10:
       print(f"นี่คือตำแนห่งคุณ:",{buys})
   else:
       print("ปิดการใช้งาน")
       break
