import sys

def getFileName(studentName, weekNumber, assignmentNumber):
    fileName = "week{0:0>2}_assignment{1:0>2}_{2}".format(
                                                    weekNumber, 
                                                    assignmentNumber, 
                                                    studentName)
    return fileName

if __name__ == '__main__':
    print(getFileName(sys.argv[1], int(sys.argv[2]), int(sys.argv[3])))
    # python week05_assignment06_student42_DangNgocQuan.py DangNgocQuan 5 6
    # week05_assignment06_DangNgocQuan