def getFileName(studentName, weekNumber, assignmentNumber):
    fileName = "week{0:0>2}_assignment{1:0>2}_{2}".format(
                                                    weekNumber, 
                                                    assignmentNumber, 
                                                    studentName)
    return fileName

if __name__ == '__main__':
    print(getFileName("DangNgocQuan", 2, 3))  #week02_assignment03_DangNgocQuan
    print(getFileName("DangNgocQuan", 2, 4))  #week02_assignment04_DangNgocQuan
    print(getFileName("DangNgocQuan", 2, 10))  #week02_assignment10_DangNgocQuan