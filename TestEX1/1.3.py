def findTrailingZeros(n):
 
    
    count = 0
 
    
    i = 5
    while (n / i >= 1):
        count += int(n / i)
        i *= 5
    
    return int(count) 
 
##เปลี่ยนเลขตรงนี้ 
n = 10

print(n,"จำนวน 0 ต่อท้าย มี " , findTrailingZeros(n))