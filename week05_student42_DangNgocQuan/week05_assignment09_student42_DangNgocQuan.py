'''Hỏi trong thời gian hoạt động của đồng hồ từ 00h00’10” đến 11h59’50” cùng ngày, giá trị 
lớn nhất và giá trị bé nhất mà M có thể đạt được là bao nhiêu?'''
'''Những giá trị đó đạt được vào (những) thời điểm nào?'''
# Ta sẽ xét 2 cách hiểu:
#   + Cách 1: ví dụ, tại thời điểm 05h30m00s thì kim giờ chỉ đúng số 5
#   + Cách 2: Ví dụ, tại thời điểm 05h30m00s thì kim giờ đang ở chính giữa số 5 và số 6

import math

# Giả sử tọa độ các kim đồng hồ nằm trong khoảng [0, 60) và tăng dần theo chiều chạy của kim đồng hồ,
# Ví dụ, 5h00m00s thì kim giờ đang ở tọa độ 25
#        0h30m00s thì kim phút đang ở tọa độ 30
# trong hàm này, x1 và x2 là tọa độ của 2 kim đồng hồ, và hàm sẽ trả về khoảng cách của 2 kim
def distance(x1, x2):
    ans = math.sqrt(2 - 2 * math.cos(2*math.pi*(math.fabs(x1-x2) / 60)))
    return ans

# Trả về giá trị của M trong thời điểm đang xét
# Tham số choice biểu thị cách tính M
# + choice = 1 thì sẽ tính theo cách hiểu 1
# + choice = 2 thì sẽ tính theo cách hiểu 2
def M(hour, minute, second, choice):
    if choice == 1:
        return distance(hour*5, minute) + distance(hour*5, second) + distance(second, minute)
    elif choice == 2:
        minute += second/60
        hour += minute/60
        return distance(hour*5, minute) + distance(hour*5, second) + distance(second, minute)
    else:
        return None

# Hàm dùng để tính giá trị M min
# + choice = 1 thì sẽ tính theo cách hiểu 1
# + choice = 2 thì sẽ tính theo cách hiểu 2
def getMmin(choice):
    Mmin = 1000000
    for totalSecond in range(10, 43191):
        hour = totalSecond // 3600
        minute = (totalSecond - 3600*hour) // 60
        second = totalSecond % 60
        Mmin = min(M(hour, minute, second, choice), Mmin)
    return Mmin

# Hàm trả về list gồm các thời điểm mà M min
# + choice = 1 thì sẽ tính theo cách hiểu 1
# + choice = 2 thì sẽ tính theo cách hiểu 2
def getListTimeMmin(choice):
    ansList = []
    Mmin = getMmin(choice)
    for totalSecond in range(10, 43191):
        hour = totalSecond // 3600
        minute = (totalSecond - 3600*hour) // 60
        second = totalSecond % 60
        if M(hour, minute, second, choice) == Mmin:
            ansList.append("{0:0>2}h{1:0>2}m{2:0>2}s".format(hour, minute, second))
    return ansList

# Hàm dùng để tính giá trị M max
# + choice = 1 thì sẽ tính theo cách hiểu 1
# + choice = 2 thì sẽ tính theo cách hiểu 2
def getMmax(choice):
    Mmax = -1
    for totalSecond in range(10, 43191):
        hour = totalSecond // 3600
        minute = (totalSecond - 3600*hour) // 60
        second = totalSecond % 60
        Mmax = max(M(hour, minute, second, choice), Mmax)
    return Mmax

# Hàm trả về list gồm các thời điểm mà M max
# + choice = 1 thì sẽ tính theo cách hiểu 1
# + choice = 2 thì sẽ tính theo cách hiểu 2
def getListTimeMmax(choice):
    ansList = []
    Mmax = getMmax(choice)
    for totalSecond in range(10, 43191):
        hour = totalSecond // 3600
        minute = (totalSecond - 3600*hour) // 60
        second = totalSecond % 60
        if M(hour, minute, second, choice) == Mmax:
            ansList.append("{0:0>2}h{1:0>2}m{2:0>2}s".format(hour, minute, second))
    return ansList       

if __name__ == '__main__':
    '''Nếu hiểu theo cách 1 thì đây là kết quả'''
    print(getMmin(1))
    # 0.0
    print(getListTimeMmin(1))
    # ['01h05m05s', '02h10m10s', '03h15m15s', '04h20m20s', '05h25m25s', '06h30m30s', 
    # '07h35m35s', '08h40m40s', '09h45m45s', '10h50m50s', '11h55m55s']
    print(getMmax(1))
    #  5.196152422706632
    print(getListTimeMmax(1))
    # ['00h20m40s', '00h40m20s', '01h25m45s', '01h45m25s', '02h30m50s', '02h50m30s', 
    # '03h35m55s', '03h55m35s', '04h00m40s', '04h40m00s', '05h05m45s', '05h45m05s', 
    # '06h10m50s', '06h50m10s', '07h15m55s', '07h55m15s', '08h00m20s', '08h20m00s', 
    # '09h05m25s', '09h25m05s', '10h10m30s', '10h30m10s', '11h15m35s', '11h35m15s']
    
    '''Nếu hiểu theo cách 2 thì đây là kết quả'''
    print(getMmin(2))
    # 0.05264969567201981
    print(getListTimeMmin(2))
    # ['02h11m11s', '09h48m49s']
    print(getMmax(2))
    # 5.19607028672883
    print(getListTimeMmax(2))
    # ['05h49m09s', '06h10m51s']
     