import pandas

def createAndSaveDataFrame01():
    dataFrame01 = pandas.DataFrame({
        "MSV" : [],
        "classCode" : [],
        "subjectCode" : []
    })
    for index in range(len(exams.index)):
        subjectCode = exams["subjectCode"][index]
        strClassCodes = exams["classCode"][index]
        classCodes = strClassCodes[1:-1].split(",")
        for classCode in classCodes:
            classCode = classCode.strip()[1:-1]
            if len(classCode) == 0:
                continue
            path = f".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\data\\examinationTimetablingDataset\\examinationTimetablingDataset\\{classCode}.csv"
            df = pandas.read_csv(path)
            for MSV in df["MSV"]:
                dataFrame01.loc[len(dataFrame01.index)] = [MSV, classCode, subjectCode]
    
    dataFrame01 = dataFrame01.sort_values(by=["MSV", "subjectCode", "classCode"])
    
    dataFrame01.to_csv(".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\output\\dataFrame01.csv", index=False)
 
    
def createAndSaveDataFrame02():
    dataFrame02 = pandas.DataFrame({
        "classCode" : [],
        "MSVList" : [],
        "numberStudents" : []
    })
    for index in range(len(exams.index)):
        subjectCode = exams["subjectCode"][index]
        strClassCodes = exams["classCode"][index]
        classCodes = strClassCodes[1:-1].split(",")
        for classCode in classCodes:
            classCode = classCode.strip()[1:-1]
            if len(classCode) == 0:
                continue
            path = f".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\data\\examinationTimetablingDataset\\examinationTimetablingDataset\\{classCode}.csv"
            df = pandas.read_csv(path)
            MSVList = df["MSV"].to_list()
            MSVList.sort()
            dataFrame02.loc[len(dataFrame02.index)] = [classCode, MSVList, len(df.index)]
    
    dataFrame02 = dataFrame02.sort_values(by=["classCode", "numberStudents"])
    dataFrame02.to_csv(".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\output\\dataFrame02.csv", index=False)


def createAndSaveDataFrame03():
    dataFrame03 = pandas.DataFrame({
        "subjectCode" : [],
        "MSVList" : [],
        "numberStudents" : []
    })
    for index in range(len(exams.index)):
        subjectCode = exams["subjectCode"][index]
        strClassCodes = exams["classCode"][index]
        classCodes = strClassCodes[1:-1].split(",")
        MSVList = []
        for classCode in classCodes:
            classCode = classCode.strip()[1:-1]
            if len(classCode) == 0:
                continue
            path = f".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\data\\examinationTimetablingDataset\\examinationTimetablingDataset\\{classCode}.csv"
            df = pandas.read_csv(path)
            MSVList += (df["MSV"].to_list())
            MSVList.sort()
        dataFrame03.loc[len(dataFrame03.index)] = [subjectCode, MSVList, len(MSVList)]
    
    dataFrame03 = dataFrame03.sort_values(by=["subjectCode", "numberStudents"])
    dataFrame03.to_csv(".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\output\\dataFrame03.csv", index=False)

def createAndSaveDataFrame04():
    dict = {
        
    }
    for index in range(len(exams.index)):
        subjectCode = exams["subjectCode"][index]
        strClassCodes = exams["classCode"][index]
        classCodes = strClassCodes[1:-1].split(",")
        for classCode in classCodes:
            classCode = classCode.strip()[1:-1]
            if len(classCode) == 0:
                continue
            path = f".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\data\\examinationTimetablingDataset\\examinationTimetablingDataset\\{classCode}.csv"
            df = pandas.read_csv(path)
            for MSV in df["MSV"]:
                if MSV in dict.keys():
                    if subjectCode not in dict[MSV][1]:
                        dict[MSV][1].append(subjectCode)
                    if classCode not in dict[MSV][0]:
                        dict[MSV][0].append(classCode)
                    dict[MSV][0].sort()
                    dict[MSV][1].sort()
                else:
                    dict[MSV] = [[classCode], [subjectCode]]
    
    dataFrame04 = pandas.DataFrame({
        "MSV" : [key for key in dict.keys()],
        "classCodeList" : [values[0] for values in dict.values()],
        "subjectCodeList" : [values[1] for values in dict.values()]
    })
    
    dataFrame04 = dataFrame04.sort_values(by=["MSV"])
    dataFrame04.to_csv(".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\output\\dataFrame04.csv", index=False)


def createAndSaveDataFrame05():
    dataFrame05 = pandas.DataFrame({
        "firstSubjectCode" : [],
        "secondSubjectCode" : [],
        "studentsSameTwoSubjects" : [],
        "numberStudents" : []
    })
    
    studentListOfSubject = []
    for index in range(len(exams.index)):
        subjectCode = exams["subjectCode"][index]
        studentList = []
        strClassCodes = exams["classCode"][index]
        classCodes = strClassCodes[1:-1].split(",")
        for classCode in classCodes:
            classCode = classCode.strip()[1:-1]
            if len(classCode) == 0:
                continue
            path = f".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\data\\examinationTimetablingDataset\\examinationTimetablingDataset\\{classCode}.csv"
            df = pandas.read_csv(path)
            studentList += (df["MSV"].to_list())
        studentListOfSubject.append(studentList)
        
    for index1 in range(len(studentListOfSubject) - 1):
        firstSubjectCode = exams["subjectCode"][index1]
        firstStudentList = studentListOfSubject[index1]
        for index2 in range(index1 + 1, len(studentListOfSubject)):
            secondSubjectCode = exams["subjectCode"][index2]
            secondStudentList = studentListOfSubject[index2]
            studentsSameTwoSubjects = list(set(firstStudentList) & set(secondStudentList))
            studentsSameTwoSubjects.sort()
            dataFrame05.loc[len(dataFrame05.index)] = [firstSubjectCode, secondSubjectCode, studentsSameTwoSubjects, len(studentsSameTwoSubjects)]
    
    dataFrame05 = dataFrame05.sort_values(by=["firstSubjectCode", "secondSubjectCode"])
    dataFrame05.to_csv(".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\output\\dataFrame05.csv", index=False)

def createAndSaveStatistical():
    dataFrame02 = pandas.read_csv(".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\output\\dataFrame02.csv")
    dataFrame03 = pandas.read_csv(".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\output\\dataFrame03.csv")
    dataFrame04 = pandas.read_csv(".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\output\\dataFrame04.csv")
    dataFrame05 = pandas.read_csv(".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\output\\dataFrame05.csv")
    
    numberStudents = len(dataFrame04.index)
    numberClasses = len(dataFrame02.index)
    numberSubjects = len(dataFrame03.index)
    averageSubjectsPerStudent = sum(len(strSubjectCodeList.split(',')) 
                                    for strSubjectCodeList in dataFrame04["subjectCodeList"].to_list()) // numberStudents
    
    maxSubjects = max(len(strSubjectCodeList.split(',')) 
                       for strSubjectCodeList in dataFrame04["subjectCodeList"].to_list())
    minSubjects = min(len(strSubjectCodeList.split(',')) 
                       for strSubjectCodeList in dataFrame04["subjectCodeList"].to_list())
    studentsWithMostSubjects = []
    studentsWithFewestSubjects = []
    for index in range(len(dataFrame04.index)):
        if len(dataFrame04["subjectCodeList"][index].split(',')) == maxSubjects:
            studentsWithMostSubjects.append(dataFrame04["MSV"][index])
        if len(dataFrame04["subjectCodeList"][index].split(',')) == minSubjects:
            studentsWithFewestSubjects.append(dataFrame04["MSV"][index])
    
    maxStudents = max(int(numStudents) for numStudents in dataFrame03["numberStudents"].to_list())
    minStudents = min(int(numStudents) for numStudents in dataFrame03["numberStudents"].to_list())
    subjectWithMostStudents = []
    subjectWithFewestStudents = []
    for index in range(len(dataFrame03.index)):
        if dataFrame03["numberStudents"][index] == maxStudents:
            subjectWithMostStudents.append(dataFrame03["subjectCode"][index])
        if dataFrame03["numberStudents"][index] == minStudents:
            subjectWithFewestStudents.append(dataFrame03["subjectCode"][index])
            
    studentsHasTwoClassesWithSameSubject = []
    for index in range(len(dataFrame04.index)):
        classCodeList = dataFrame04["classCodeList"][index].split(',')
        subjectCodeList = dataFrame04["subjectCodeList"][index].split(',')
        if len(classCodeList) > len(subjectCodeList):
            studentsHasTwoClassesWithSameSubject.append(dataFrame04["MSV"][index])
    
    maxStudentsInCommon = max(int(numStudents) for numStudents in dataFrame05["numberStudents"].to_list())
    twoSubjectsWithMostStudentsInCommon = []
    for index in range(len(dataFrame05.index)):
        if int(dataFrame05["numberStudents"][index]) == maxStudentsInCommon:
            twoSubjectsWithMostStudentsInCommon.append([dataFrame05["firstSubjectCode"][index], dataFrame05["secondSubjectCode"][index]])

    statisticalData = pandas.DataFrame({
        "numberStudents" : [numberStudents],
        "numberClasses" : [numberClasses],
        "numberSubjects" : [numberSubjects],
        "averageSubjectsPerStudent" : [averageSubjectsPerStudent],
        "studentsWithMostSubjects" : [studentsWithMostSubjects],
        "studentsWithFewestSubjects" : [studentsWithFewestSubjects],
        "subjectWithMostStudents" : [subjectWithMostStudents],
        "subjectWithFewestStudents" : [subjectWithFewestStudents],
        "studentsHasTwoClassesWithSameSubject" : [studentsHasTwoClassesWithSameSubject],
        "twoSubjectsWithMostStudentsInCommon" : [twoSubjectsWithMostStudentsInCommon]
    })
    statisticalData.to_csv(".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\output\\statisticalData.csv", index=False)

if __name__ == '__main__':
    '''a) Tạo các DataFrame được liệt kê ở trên, chọn tên biến và tên cột phù hợp. 
    Ngoài ra, các dòng trong mỗi DataFrame cũng nên được sắp xếp theo một thứ tự hợp lý.'''
    
    path01 = ".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\data\\exams.csv"
    exams = pandas.read_csv(path01)
    
    '''1. DataFrame thứ nhất
            Cột 1: một mã sinh viên
            Cột 2: một mã lớp học mà sinh viên đó đăng ký
            Cột 3: một mã môn học tương ứng với mã lớp học kể trên'''
    createAndSaveDataFrame01()
    
    '''2. DataFrame thứ hai
            Cột 1: một mã lớp học
            Cột 2: một list tất cả mã sinh viên đăng ký lớp học đó
            Cột 3: số sinh viên đăng ký lớp học đó'''
    createAndSaveDataFrame02()
    
    '''3. DataFrame thứ ba
            Cột 1: một mã môn học
            Cột 2: một list tất cả mã sinh viên đăng ký môn học đó
            Cột 3: số sinh viên đăng ký môn học đó'''     
    createAndSaveDataFrame03()
    
    '''4. DataFrame thứ tư
            Cột 1: một mã sinh viên
            Cột 2: một list tất cả lớp học mà sinh viên đó đăng ký
            Cột 3: một list tất cả môn học mà sinh viên đó đăng ký'''
    createAndSaveDataFrame04()
    
    '''5. DataFrame thứ năm
            Cột 1: một mã môn học
            Cột 2: một mã môn học (nên khác với giá trị ở cột 1)
            Cột 3: một list tất cả sinh viên cùng đăng ký hai môn học kể trên
            Cột 4: số sinh viên cùng đăng ký hai môn học kể trên'''
    createAndSaveDataFrame05()
    
    
    '''b) Xuất những DataFrame này (với định dạng file phù hợp) vào thư mục bổ sung trong thư mục nộp bài.'''
    # Các dataFrame sẽ được lưu ở folder additionalFolder\\assignment06\\output
    
    
    '''c) Thống kê các thông tin liên quan tới bộ dữ liệu trên (càng nhiều càng tốt). 
    Dưới đây là gợi ý cho một số khía cạnh của bộ dữ liệu.
            Số sinh viên, lớp học, môn học của học kỳ.
            Số môn trung bình một sinh viên đăng ký.
            Sinh viên đăng ký nhiều môn học nhất, ít môn học nhất.
            Môn học có nhiều (hoặc ít) sinh viên đăng ký nhất.
            Có sinh viên nào học hai lớp có chung mã môn hay không?
            Hai môn học có chung nhiều sinh viên nhất.'''
    createAndSaveStatistical()
    # Các số liệu thống kê sẽ được lưu ở folder additionalFolder\\assignment06\\output\\statisticalData.csv