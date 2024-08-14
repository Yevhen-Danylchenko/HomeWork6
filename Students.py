students = [
    ('Alice', 87),
    ('Bob', 87),
    ('Mark', 65),
    ('Den', 75),
    ('Ilya', 60),
    ('Oleg',90)
]

my_dict_students = {}
name = ''
number = 0

def My_Func() :
    for num1, num2 in students :
            name = num1
            number = num2

            my_dict_students.update({number:name})

    print(my_dict_students)


My_Func()







