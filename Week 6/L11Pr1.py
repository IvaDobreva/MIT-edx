def genPrimes():
    numbers = []
    num = 2
    
    while True:
        for c in range(2, num+1):
            if num%c == 0:
                break
        if num == c:
            numbers.append(num)
            yield num
        num+=1
