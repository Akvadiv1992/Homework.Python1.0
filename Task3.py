print("Введите шестизначное число: ")
a = int(input())

a1 =int (a / 100000) # 1 цифра
a2 =int (a / 10000) 
a2 = a2 % 10         # 2 цифра
a3 =int (a / 1000)
a3 = a3 % 10         # 3 цифра
a4 = int (a / 100)
a4 = a4 % 10         # 4 цифра
a5 = int (a / 10)
a5 = a5 % 10         # 5 цифра
a6 = a % 10          # 6 цифра

if a1 + a2 + a3 == a4 + a5 + a6:
    print(a,"--> yes")
else:
    print(a, "--> no")