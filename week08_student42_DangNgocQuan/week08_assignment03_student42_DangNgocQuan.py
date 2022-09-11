import datetime
import random
import pandas

if __name__ == '__main__':
    """a) Tạo một DataFrame gồm một nghìn dòng và một cột timestamp với giá trị mỗi ô là một 
    thời điểm ngẫu nhiên trong năm 2022."""
    
    dataframe = pandas.DataFrame({
        'timestamp' : []
    })
    startTime = datetime.datetime(2022, 1, 1, 0, 0, 0)
    for i in range(1000):
        dayDelta = random.randint(0, 364)
        secondDelta = random.randint(0, 86399)
        randomDatetime = startTime + datetime.timedelta(days=dayDelta, seconds=secondDelta)
        dataframe.loc[i] = randomDatetime
    print(dataframe)
    #             timestamp
    # 0   2022-02-20 20:07:56
    # 1   2022-01-18 01:41:24
    # 2   2022-01-27 05:57:17
    # 3   2022-04-01 02:20:27
    # 4   2022-11-07 19:39:00
    # ..                  ...
    # 995 2022-06-18 00:28:01
    # 996 2022-09-27 02:26:46
    # 997 2022-05-26 04:23:54
    # 998 2022-03-13 15:21:12
    # 999 2022-07-08 23:14:36

    # [1000 rows x 1 columns]
    
    """b) Bổ sung cột date vào DataFrame kể trên, trong đó chỉ lưu giá trị ngày tương ứng với 
    giá trị của cột timestamp. Tìm cách tối ưu hóa thời gian thực thi công việc này."""
    date = []
    for i in range(1000):
        date.append(dataframe['timestamp'][i].date())
    dataframe['date'] = date
    print(dataframe)
    #             timestamp        date
    # 0   2022-02-20 20:07:56  2022-02-20
    # 1   2022-01-18 01:41:24  2022-01-18
    # 2   2022-01-27 05:57:17  2022-01-27
    # 3   2022-04-01 02:20:27  2022-04-01
    # 4   2022-11-07 19:39:00  2022-11-07
    # ..                  ...         ...
    # 995 2022-06-18 00:28:01  2022-06-18
    # 996 2022-09-27 02:26:46  2022-09-27
    # 997 2022-05-26 04:23:54  2022-05-26
    # 998 2022-03-13 15:21:12  2022-03-13
    # 999 2022-07-08 23:14:36  2022-07-08

    # [1000 rows x 2 columns]
    
    dataframe.to_csv('./week08_student42_DangNgocQuan/additionalFolder/assignment03/dataframe.csv')