students = {
    'Alice': 87,
    'Bob' : 87,
    'Mark': 65,
    'Den': 75,
    'Ilya': 60,
    'Oleg': 90
}

a = 0
numSum = 0

def My_Func (numSum, a) :
    for i in students :
        numSum += students[i]
        a += 1
    tmp = numSum / a
    print(tmp)

My_Func(numSum, a)