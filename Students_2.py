students = [
    ('Alice', 87),
    ('Bob', 87),
    ('Mark', 65),
    ('Den', 75),
    ('Ilya', 60),
    ('Oleg',90)
]

my_dict_students = {}

def My_Func(my_dict_students) :
    for num1, num2 in students :
        if num2 not in my_dict_students :
            my_dict_students[num2] = []

        my_dict_students[num2].append(num1)

    print(my_dict_students)

My_Func(my_dict_students)