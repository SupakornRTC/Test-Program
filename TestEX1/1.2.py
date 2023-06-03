index = [1,2,1,3,5,6,4]

largest_number = None

for i in index:
    if largest_number is None or largest_number < i:
        largest_number = i


print('ค่ามากที่สุดคือ =',largest_number)    
print('ค่ามากที่สุดคือ index ที่ =',index.index(largest_number))  

