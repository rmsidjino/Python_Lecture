def sum_num(*args):
    sum = 0
    data = 0
    for number in args:
        data += 1
        sum += number
    
    print("3개의 인자" ,args)
    print("합계 : {0} , 평균 : {1}".format(sum, sum/data))

print(sum_num(10,20,30))