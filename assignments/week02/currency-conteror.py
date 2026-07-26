#Cosde
print("1. THB to USD")
print("2. USD to THB")
choice = input("Please Choose")
if choice =="1":
    THB = float(input("Amount:"))
    THB_USD = THB / 35.5
    print("Formula used: THB / 35.5")
    print("แปลงค่าเงินได้", round(THB_USD, 2), "USD")
elif choice =="2":
    USD = float(input("Amount:"))
    USD_THB = USD * 35.5
    print("Formula used: USD * 35.5")
    print("แปลงค่าเงินได้", round(USD_THB, 2), "THB")