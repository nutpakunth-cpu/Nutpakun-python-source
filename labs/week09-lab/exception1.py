# เครื่องคำนวณอย่างปลอดภัย

try:
    num1 = float(input("ตัวเลขที่ 1: "))
    num2 = float(input("ตัวเลขที่ 2: "))
    operator = input("เครื่องหมาย (+, -, *, /): ")  

    if operator not in ["+", "-", "*", "/"]:
        raise ValueError("เครื่องหมายไม่ถูก")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2

    print(f"ผลลัพธ์ = {result}")

except ValueError as error:
    print(f"ข้อมูลไม่ถูก: {error}")

except ZeroDivisionError as error:
    print("ไม่สามารถหารด้วยศูนย์ได้")

finally:
    print("จบการทำงาน")


