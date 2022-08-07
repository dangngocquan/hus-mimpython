def sort2(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst) - 1):
            if min(lst[j]) > min(lst[j+1]):
                x = lst[j+1]
                lst[j+1] = lst[j]
                lst[j] = x

def sort1(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst) - 1):
            if sum(lst[j]) > sum(lst[j+1]):
                x = lst[j+1]
                lst[j+1] = lst[j]
                lst[j] = x

if __name__ == '__main__':
    lst = [[1,2], [3,0,4], [2], [4,5]]
    sort1(lst)
    print(lst)
    
    lst2 = [[1, 2, 3, 4], [-1, 2], [-3, 5, 4], [1, 2, 5, 3], [1, 0, 2]]
    sort2(lst2)
    print(lst2)              
    
    