import array as arr

numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = arr.array('i', numbers_list)

print(numbers_array[2:5])  # 3rd to 5th
print(numbers_array[:-5])  # beginning to 4th
print(numbers_array[5:])   # 6th to end
print(numbers_array[:])

print(numbers_array[6:7])


[print(i/2) for i in numbers_array]



x=2
f = lambda x : x+2

print(eval("x+2"))

eval(x)