# ✅ Complete this function, replace `pass` with your solution:
def find_min_max(numbers) -> dict:
    min = numbers[0]
    max = numbers[0]
    for num in numbers:
        if min > num:
            min = num
        if max < num:
            max = num 
    return {'min': min , 'max':max}

    





############### ❌ DO NOT change these lines ###############
list1 = [1, 2, 3, 2, -1, 5]
list2 = [21, 2.5, -3, -2, -1, 5.1]

result1 = find_min_max(list1)
result2 = find_min_max(list2)

print(result1)  # --> {'min': -1, 'max': 5}
print(result2)  # --> {'min': -3, 'max': 21}
############### ❌ DO NOT change these lines ###############