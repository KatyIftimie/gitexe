numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
# numbers = [2, 3, 5]
ma = numbers[0]
mi = numbers[0]
sum_element = 0
aver = [0]
leng = len(numbers)

i = 1
while i<len(numbers):
    if numbers[i]>ma:
        ma= numbers[i]
    i= i+1
while i<len(numbers):
    if numbers[i]<mi:
        mi= numbers[i]
    i= i+1
    
for i in range(len(numbers)):
    sum_element = numbers[i] + sum_element
    
aver = sum_element/ leng
print(ma, mi, aver)