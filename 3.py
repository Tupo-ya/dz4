nums = [int(i) for i in input('Введите числа через пробел: ').split()]
deg = int(input('Степень: '))

for i in range(len(nums)):
    nums[i] = nums[i]**deg

print(nums)