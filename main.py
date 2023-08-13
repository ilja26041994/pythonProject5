# try:
#     someLogin = input('enter your login: ')
#     if len(someLogin) <= 2:
#         raise Exception('length of yor login must be more than 3')
#     elif len(someLogin) >= 30:
#         raise Exception('length of yor login must be less than 30 symbols')
# except Exception as ex:
#     print(ex)
# try:
#     somePassword = input('enter your password: ')
#     if len(somePassword) < 8:
#         raise Exception('length of your password mus be at least 8 symbols')
# except Exception as ex:
#     print(ex)
# print(someLogin, somePassword)

# сортировка пузырьком ввод параметров через try-except

try:
    lenList = int(input('enter lenght of list:'))
except: Exception('length of list must be integer')

try:
    list =[]
    for i in range(lenList):
        list.append(int(input('enter number:')))
except Exception as e:
    print(e)
print(list)
try:
    cnt = 0
    for run in range(lenList -1):
        for i in range(lenList - 1 - run):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                cnt += 1
                print(list[i], list[i + 1])
        print(list)
        print(cnt)

except Exception as e:
    print(e)
