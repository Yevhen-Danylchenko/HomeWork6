my_tuple = (1,4,56,24,80,250,8,60,2,3)

sumNum = my_tuple[0]
i = 0
value = 0

def My_Func (sumNum, i, value) :
    for index in my_tuple :
        sumNum += index
        i += 1
    value = sumNum / i

    return value

print(My_Func (sumNum, i, value))

My_Func(sumNum, i, value)