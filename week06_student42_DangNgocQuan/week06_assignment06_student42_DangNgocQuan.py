import pandas

if __name__ == '__main__':
    '''a) Tạo các DataFrame được liệt kê ở trên, chọn tên biến và tên cột phù hợp. 
    Ngoài ra, các dòng trong mỗi DataFrame cũng nên được sắp xếp theo một thứ tự hợp lý.'''
    path01 = ".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\data\\exams.csv"
    exams = pandas.read_csv(path01)
    
    '''1. DataFrame thứ nhất
            Cột 1: một mã sinh viên
            Cột 2: một mã lớp học mà sinh viên đó đăng ký
            Cột 3: một mã môn học tương ứng với mã lớp học kể trên'''
    
    # dataFrame01 = pandas.DataFrame({
    #     "MSV" : [],
    #     "classCode" : [],
    #     "subjectCode" : []
    # })
    
    # for index in range(len(exams.index)):
    #     subjectCode = exams["subjectCode"][index]
    #     strClassCodes = exams["classCode"][index]
    #     classCodes = strClassCodes[1:-1].split(",")
    #     for classCode in classCodes:
    #         classCode = classCode.strip()[1:-1]
    #         if len(classCode) == 0:
    #             continue
    #         path = f".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\data\\examinationTimetablingDataset\\examinationTimetablingDataset\\{classCode}.csv"
    #         df = pandas.read_csv(path)
    #         for MSV in df["MSV"]:
    #             dataFrame01.loc[len(dataFrame01.index)] = [MSV, classCode, subjectCode]
    
    # dataFrame01 = dataFrame01.sort_values(by=["MSV", "subjectCode", "classCode"])
    
    # dataFrame01.to_csv(".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\output\\dataFrame01.csv", index=False)
    
    
    
    '''2. DataFrame thứ hai
            Cột 1: một mã lớp học
            Cột 2: một list tất cả mã sinh viên đăng ký lớp học đó
            Cột 3: số sinh viên đăng ký lớp học đó'''
    
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
            dataFrame02.loc[len(dataFrame02.index)] = [classCode, df["MSV"].to_list(), len(df.index)]
    
    dataFrame02 = dataFrame02.sort_values(by=["classCode", "numberStudents"])
    dataFrame02.to_csv(".\\week06_student42_DangNgocQuan\\additionalFolder\\assignment06\\output\\dataFrame02.csv", index=False)