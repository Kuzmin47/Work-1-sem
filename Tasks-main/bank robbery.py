a = [("sber", 100), ("ZXC", 1), ("VTB", 1), ("Alfa", 100)] 
n = len(a) 
if n == 0: print("Максимально денег украдено: 0\nОграблено банков: нет банков\nНомера ограбленных банков: нет банков") 
else:
    с = [0]*n 
    с[0] = a[0][1]
    if n>1:с[1] = max(a[0][1],a[1][1])
    for i in range(2,n): с[i]=max(с[i-1],с[i-2]+a[i][1]) 
    money = с[-1]
    chosen,i=[],n-1 
    while i >= 0:
        if i == 0 or с[i] != с[i - 1]:
            chosen.append(a[i]) 
            i -= 2 
        else: i -= 1
    chosen.reverse() 
 
    banks = [bank[0] for bank in chosen] 
    print(f'Максимально денег украдено: {money}\nОграблено банков: {banks}\nНомера ограбленных банков: {[a.index(bank) for bank in chosen]}')