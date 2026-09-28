try:
    n = int(input())
    dic = dict()
    for i in range(1,n+1):
        dic[i] = i*i
    print(dic)

except ValueError:
    print("Invalid Input")
