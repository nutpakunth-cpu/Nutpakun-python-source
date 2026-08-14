""" 
เขียน FUNCTION แปลงหน่วยสกุลเงิน ที่สามารถแปลงเงินจาก
THB <-> USD .. 1 USD = 32 THB 

โดยใช้ชื้อและการใช้งาน
function convert_currency(100, "USD")

แสดงผลออกทางหน้าจอ
100 THB = 3.3 USD

และทดสอบการใช้งาน function ที่ตัวเองเขียนด้วย

"""

def convert_currency(amount, currency):
    if currency == "USD":
        print(f"{amount} THB = {amount / 32:.1f} USD")
    else:
        print(f"{amount} USD = {amount * 32} THB")

convert_currency(100, "USD")