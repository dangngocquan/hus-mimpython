# Hàm sắp xếp list theo thứ tự tăng dần của tổng các số trong mỗi list con
def sortByCondition01(inputList):
    for turn in range(len(inputList)):
        for index in range(len(inputList) - 1):
            if sum(inputList[index]) > sum(inputList[index+1]):
                tempList = inputList[index]
                inputList[index] = inputList[index+1]
                inputList[index+1] = tempList

# Hàm sắp xếp list theo thứ tự tăng dần của giá trị lớn nhất trong mỗi list con
def sortByCondition02(inputList):
    for turn in range(len(inputList)):
        for index in range(len(inputList) - 1):
            if max(inputList[index]) > max(inputList[index+1]):
                tempList = inputList[index]
                inputList[index] = inputList[index+1]
                inputList[index+1] = tempList

if __name__ == '__main__':
    inputList1 = [[1,2], [3,0,4], [2], [4,5]]
    sortByCondition01(inputList1)
    print(inputList1)               # [[2], [1, 2], [3, 0, 4], [4, 5]]
    
    inputList2 = [[1, 1, 0, 1], [2, 2], [11, 0, 4], [0, 0, 1, 3], [1, 0, 2]]
    sortByCondition01(inputList2)
    print(inputList2)               # [[1, 1, 0, 1], [1, 0, 2], [2, 2], [0, 0, 1, 3], [11, 0, 4]]
    
    '''Yêu cầu bổ sung: đặt ra thêm tiêu chí để so sánh hai list ổn bất kỳ và áp dụng tiêu chí này để 
    sắp xếp list đầu vào.'''
    inputList3 = [[1,2], [3,0,4], [2], [4,5]]
    sortByCondition02(inputList3)
    print(inputList3)               # [[1, 2], [2], [3, 0, 4], [4, 5]]
    
    inputList4 = [[1, 1, 0, 1], [2, 2], [11, 0, 4], [0, 0, 1, 3], [1, 0, 2]]
    sortByCondition02(inputList4)
    print(inputList4)               # [[1, 1, 0, 1], [2, 2], [1, 0, 2], [0, 0, 1, 3], [11, 0, 4]]
    
    
    