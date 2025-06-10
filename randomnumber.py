import random 

def guess_number():
    #กำหนดตัวเลขสุ่ม 1 ถึง 2000
    number = random.randint(1, 20)
    
    #กำหนดเริ่มต้นของตัวเลขที่ผู้ใช้จะทาย
    numstart = 0
    
    #เลขเริ่มต้นที่ผู้ทายจะทาย
    userguess = 0
    
    print("ยินดีต้อนรับสู่เกมทายเลขของ นาย ทรงเดช จำปาเทศ")
    print("ทายเลข 1 ถึง 20")
    print("-------------------------------------")
    
    #ลูปจนกว่าจะทายถูก
    while userguess != number:
        try:
            
            #รับค่าจากผู้ทาย
            userguess = int(input("เลขที่ท่านจะทายคืืออะไร :  "))
            
            #เพิ่มจจำนวนครั้งที่ทาย
            numstart += 1
            
            #ตรวจสอบว่าผู้ทายทายถูกหรือไม่
            if userguess < number:
                print("เลขที่ท่านทายต่ำกว่าที่กำหนด")
            elif userguess > number:
                print("เลขที่ท่านทายสูงกว่าที่กำหนด")
            else:
                print("ทายถูกต้องแล้ว")
                print(f"จำนวนครั้งที่ท่านทายคือ {numstart} ครั้ง")
                print("ขอบคุณที่เล่นเกมนี้ ")
                break
            
        #หากผู้ใช้ใส่ค่าที่ไม่ใช่ตัวเลข
        except ValueError:
            print("กรุณาใส่ตัวเลขที่ถูกต้อง")

#เริ่มเกม
if __name__ == "__main__":
    guess_number()