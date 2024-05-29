print(10+3)

numbers = [1, 2, 3]
# numbers.

# for item in numbers:
#     print(item)

for item in range(3, 5):
    print(item)

print (numbers)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = [x*x for x in nums if x % 2 == 0]
print (my_list)

my_dict = {'%d'%x: x for x in nums}
print(my_dict)
my_set = {x % 2 for x in nums}
print(my_set)

