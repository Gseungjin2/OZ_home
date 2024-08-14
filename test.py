def sum_int(start, end,):
    total = 0
    for i in range(start, end + 1):  
        total += i
    print("%d~%d 정수 합계 : %d" % (start, end, total))

sum_int(30, 50)
sum_int(500, 600)