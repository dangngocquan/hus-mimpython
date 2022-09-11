import random
import pandas


if __name__ == '__main__':
    """a) Tạo ngẫu nhiên một DataFrame chứa dữ liệu về điểm trung bình của sinh viên. Dữ liệu cần có 
    tối thiểu ba trường thông tin name, class, score."""
    
    names = ['An', 'Anh', 'Dai', 'Dat', 'Diep', 'Du', 'Duc', 'Dung', 'Giang', 'Hai', 'Hao', 'Hiep', 'Hieu',
            'Hoang', 'Huy', 'Huyen', 'Lam', 'Le', 'Liem', 'Linh', 'Long', 'Luat', 'Ly', 'Minh', 'Nam',
            'Nghia', 'Ngoc', 'Nhat', 'Phuc', 'Phuong', 'Quan', 'Quynh', 'Sang', 'Son', 'Tai', 'Tam', 'Thai',
            'Thang', 'Thanh', 'Thao', 'Thien', 'Trung', 'Tu', 'Tuan', 'Tung', 'Uy', 'Van']
    classes = ['K67', 'K66', 'K65', 'K64', 'K63', 'K62', 'K61']
    
    dataframe1 = pandas.DataFrame({
        'name' : [],
        'class' : [],
        'score' : []
    })
    
    for i in range(60):
        name = random.choice(names)
        classs = random.choice(classes)
        score = random.randint(0, 100) / 10
        dataframe1.loc[i] = [name, classs, score]
    
    dataframe1.to_csv('./week08_student42_DangNgocQuan/additionalFolder/assignment04/dataframe01.csv')
    
    
    """b) Thống kê điểm sinh viên theo từng lớp, trình bày thống kê trong một DataFrame với ít nhất ba 
    cột class, nStudents, meanScore."""
    
    dict = {}
    
    for i in range(len(dataframe1.index)):
        name = dataframe1['name'][i]
        classs = dataframe1['class'][i]
        score = dataframe1['score'][i]
        if classs in dict.keys():
            dict[classs]['name'].append(name)
            dict[classs]['score'].append(score)
        else:
            dict[classs] = {
                'name' : [name],
                'score' : [score]
            }
   
    dataframe2 = pandas.DataFrame({
        'class' : [],
        'nStudents' : [],
        'meanScore' : []
    })
    
    for classs in dict.keys():
        names = dict[classs]['name']
        scores = dict[classs]['score']
        dataframe2.loc[len(dataframe2.index)] = [classs, len(names), sum(scores) / len(scores)]
    dataframe2 = dataframe2.sort_values(by=['class'])
        
    dataframe2.to_csv('./week08_student42_DangNgocQuan/additionalFolder/assignment04/dataframe02.csv')