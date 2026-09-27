def deposit(money):
    balance = 1000
    try:
        amount = float(money) 

        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0 ครับ")

    except ValueError as e: #เชคเออเร่อ

        if "ต้องมากกว่า 0" in str(e):
            print(f"\nเกิดข้อผิดพลาด: {e}")
        else:
            print(f"\nเกิดข้อผิดพลาด: กรอกตัวเลขเท่านั้น")
    else: 
        balance += amount
        print("\nฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {balance:.2f} บาท")
    finally:
        print("สิ้นสุดรายการฝากเงิน")
print("ยอดเงินเริ่มต้้น 1000 บาท")
user_input = input("กรอกจำนวนเงินที่ต้องการจะฝาก: ")
deposit(user_input)


        