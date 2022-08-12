import datetime

'''a) Giá cổ phiếu nhận giá trị là một số thực.'''
def getDate01():
    answerDatetime = datetime.date(2022, 8, 7)
    startPrice = 7.24
    tempPrice = startPrice
    finishPrice = 58.69
    maxPercent = 1.07
    while tempPrice < finishPrice:
        answerDatetime += datetime.timedelta(1)
        tempPrice *= maxPercent
    return answerDatetime

'''b) Giá cổ phiếu (đơn vị nghìn đồng) là một số có hai chữ số sau dấu chấm thập phân, ví dụ 32.40.'''
def getDate02():
    answerDatetime = datetime.date(2022, 8, 7)
    startPrice = 7.24
    tempPrice = startPrice
    finishPrice = 58.69
    maxPercent = 1.07
    while tempPrice < finishPrice:
        answerDatetime += datetime.timedelta(1)
        tempPrice *= maxPercent
        tempPrice = int(tempPrice*100) / 100
    return answerDatetime
           
if __name__ == "__main__":
    print(getDate01())      # 2022-09-07
    print(getDate02())      # 2022-09-08