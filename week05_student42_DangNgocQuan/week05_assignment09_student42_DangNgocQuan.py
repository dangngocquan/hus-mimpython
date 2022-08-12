'''Hỏi trong thời gian hoạt động của đồng hồ từ 00h00’10” đến 11h59’50” cùng ngày, giá trị 
lớn nhất và giá trị bé nhất mà M có thể đạt được là bao nhiêu?'''
# 0 <= M <= 3*(3**(1/2))
# Giá trị nhỏ nhất min M = 0
# Giá trị lớn nhất max M = 3*(3**(1/2))

'''Những giá trị đó đạt được vào (những) thời điểm nào?'''
# Thời điểm M = 0
from turtle import home


def getListTimeMmin():
    ansList = []
    for totalSecond in range(10, 43191):
        hour = totalSecond // 3600
        minute = (totalSecond - 3600*hour) // 60
        second = totalSecond % 60
        if (5*hour == minute and minute == second):
            ansList.append("{0:0>2}h{1:0>2}m{2:0>2}s".format(hour, minute, second))
    return ansList

# Thời điểm M = 3*(3**(1/2))
def getListTimeMmax():
    ansList = []
    for totalSecond in range(10, 43191):
        hour = totalSecond // 3600
        minute = (totalSecond - 3600*hour) // 60
        second = totalSecond % 60
        tempList = [hour*5, minute, second]
        tempList.sort()
        if tempList[0] + 20 == tempList[1] and tempList[1] + 20 == tempList[2]:
            ansList.append("{0:0>2}h{1:0>2}m{2:0>2}s".format(hour, minute, second))
    return ansList

if __name__ == '__main__':
    print(getListTimeMmin())
    # ['01h05m05s', '02h10m10s', '03h15m15s', '04h20m20s', '05h25m25s', '06h30m30s',
    # '07h35m35s', '08h40m40s', '09h45m45s', '10h50m50s', '11h55m55s']
    print(getListTimeMmax())
    # ['00h20m40s', '00h40m20s', '01h25m45s', '01h45m25s', '02h30m50s', '02h50m30s', 
    # '03h35m55s', '03h55m35s', '04h00m40s', '04h40m00s', '05h05m45s', '05h45m05s', 
    # '06h10m50s', '06h50m10s', '07h15m55s', '07h55m15s', '08h00m20s', '08h20m00s', 
    # '09h05m25s', '09h25m05s', '10h10m30s', '10h30m10s', '11h15m35s', '11h35m15s']   