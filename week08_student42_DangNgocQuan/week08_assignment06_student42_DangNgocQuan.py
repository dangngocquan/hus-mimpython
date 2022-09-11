if __name__ == '__main__':
    ans = 0
    countMax = 1
    for i in range(1000001):
        print(i)
        num = i
        count = 1
        while num > 1:
            count += 1
            if num % 2 == 0:
                num //= 2
            else:
                num = 3*num + 1
        if count > countMax:
            countMax = count
            ans = i
    print(ans)    # 837799