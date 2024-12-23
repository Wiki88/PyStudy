# More about the functions. Подробнее о функциях

data_structure = [

  [1, 2, 3],

  {'a': 4, 'b': 5},

  (6, {'cube': 7, 'drum': 8}),

  "Hello",

  ((), [{(2, 'Urban', ('Urban2', 35))}])

]
# print(data_structure)

def calculate_structure_sum(data_structure):
    sum_ = 0
    for i in data_structure:
        if isinstance(i, (int)) :
            sum_ += i
        if isinstance(i, str):
            sum_ += len(i)
        if isinstance(i, (list, tuple, set)):
            sum_ += calculate_structure_sum(i)
        if isinstance(i, dict):
            sum_ += calculate_structure_sum(list(i.values()))
        if isinstance(i, dict):
           sum_ += calculate_structure_sum(list(i.keys()))
    return sum_

result = calculate_structure_sum(data_structure)
print(result)
