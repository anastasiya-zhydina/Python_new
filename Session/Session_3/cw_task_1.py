# Дан список чисел, определить сколько в нем встречается различных чисел.

list = [1,2,2,4,5,5,7,0,9,0]
print(list[:])

# total_count= 0
# flag = True
# for i in range(len(list)-1):
#     for j in range(i+1, len(list)):
#         if list[i] == list[j]:
#             flag = False
#     if flag:
#         total_count+= 1
# print(total_count)

list2 = set(list)
print(list2)
print(len(list2))