list = []

while True:
    num = input()

    if num == 'sum':
        print(sum(list))
        break
    
    if num == 'mult':
        mult = 1
        
        for i in list:
            mult *= i
            
        print(mult)
        break

    list.append(int(num))
    
