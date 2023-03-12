n = int(input("введите n: "))
m = int(input("введите m: "))
k = int(input("отломить долек: "))

if k < n * m and ((k % n == 0) or (k % m == 0)):
    print(n, m, k,'--> yes')
else:
    print(n, m, k,'--> no')