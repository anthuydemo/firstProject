# a,b = 0,1
# while a < 10:
#     print(a)
#     a,b = b, a+b

# while(True):
#     x = int(input("Please enter an integer: "))
#     print(x)
#     if x < 0:
#         x = 0
#         print("Negative value changed to zero")
#     elif x == 0:
#         print("Zero")
#     elif x == 1:
#         print("Single")
#     else:
#         print("More") 
# 
       
# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(a[i])

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for x in users:
    print(x)

newUsers = users.copy()
for x in newUsers:
    print(x)
