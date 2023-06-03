
"""
Convert Number to Thai Text.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
arr = ['ศูนย์','หนึ่ง','สอง','สาม','สี่','ห้า','หก','เจ็ด','แปด','เก้า']

def number_2_word(n):

    
    if(n==0):
        return ""
    
    else:
        
        small_ans = arr[n%10]

       
        ans = number_2_word(int(n/10)) + small_ans + " "
    
    
    return ans

n = int(input('กรอกตัวเลข -->    '))
if n >=0 and n <= 10000000 :
    print("เลขที่กรอกคือ : ", n)
    print("แปลงค่าจากตัวเลขเป็นตัวอักษร : ",end="")
    print(number_2_word(n))
else : 
    print('ค่าที่กรอกคือ',n,'ต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่าเท่ากับ 10 ล้าน')