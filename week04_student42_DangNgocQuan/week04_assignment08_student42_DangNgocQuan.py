from datetime import datetime


class Datetime:
    def __init__(self, year, month, day, hour, minute, second):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        
    def __repr__(self):
        return "{0}/{1:0>2}/{2:0>2} {3:0>2}:{4:0>2}:{5:0>2}".format(self.year,
                                                                    self.month,
                                                                    self.day,
                                                                    self.hour,
                                                                    self.minute,
                                                                    self.second)
        
    def previous(self, year = 0, month = 0, day = 0, hour = 0, minute = 0, second = 0):
        numberOfDayInMonth1 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        numberOfDayInMonth2 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        while second > self.second:
            second -= 60
            minute += 1
        while minute > self.minute:
            minute -= 60
            hour += 1
        while hour > self.hour:
            hour -= 24
            day += 1
        self.second -= second
        self.minute -= minute
        self.hour -= hour
        while day > 0:
            day -= 1
            self.day -= 1
            if self.day < 1:
                self.month -= 1
                if self.month < 1:
                    self.year -= 1
                    self.month = 12
                    self.day = 31
                else:
                    if Datetime.isLeapYear(self.year):
                        self.day = numberOfDayInMonth2[self.month]
                    else:
                        self.day = numberOfDayInMonth1[self.month]
        while month > self.month:
            month -= 12
            year += 1
        self.month -= month
        self.year -= year
        if Datetime.isLeapYear(self.year):
            if self.day > numberOfDayInMonth2[self.month]:
                self.day = numberOfDayInMonth2[self.month]
        else:
            if self.day > numberOfDayInMonth1[self.month]:
                self.day = numberOfDayInMonth1[self.month]
                
    def next(self, year = 0, month = 0, day = 0, hour = 0, minute = 0, second = 0):
        numberOfDayInMonth1 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        numberOfDayInMonth2 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        while second > 59 - self.second:
            second -= 60
            minute += 1
        while minute > 59 - self.minute:
            minute -= 60
            hour += 1
        while hour > 23 - self.hour:
            hour -= 24
            day += 1
        while day > 0:
            day -= 1
            self.day += 1
            if Datetime.isLeapYear(self.year):
                if self.day > numberOfDayInMonth2[self.month]:
                    self.day = 1
                    month += 1
            else:
                if self.day > numberOfDayInMonth1[self.month]:
                    self.day = 1
                    month += 1
        while month > 12 - self.month:
            month -= 12
            year += 1
        self.month += month
        self.year += year
        if Datetime.isLeapYear(self.year):
            if self.day > numberOfDayInMonth2[self.month]:
                self.day = numberOfDayInMonth2[self.month]
        else:
            if self.day > numberOfDayInMonth1[self.month]:
                self.day = numberOfDayInMonth1[self.month]
            
    @staticmethod
    def isLeapYear(year):
        if year % 4 == 0:
            if year % 100 != 0:
                return True
            else:
                return year % 400 == 0
        return False
        
if __name__ == '__main__':
    datetime1 = Datetime(2022, 8, 6, 13, 31, 9)
    print(datetime1)                            # 2022/08/06 13:31:09
    datetime1.previous(0, 0, 0, 0 , 0, 9)   
    print(datetime1)                            # 2022/08/06 13:31:00
    datetime1.previous(0, 0, 0, 0 , 0, 1)   
    print(datetime1)                            # 2022/08/06 13:30:59
    datetime1.previous(0, 0, 0, 0 , 31, 0)   
    print(datetime1)                            # 2022/08/06 12:59:59
    datetime1.previous(0, 0, 0, 13 , 0, 0)   
    print(datetime1)                            # 2022/08/05 23:59:59
    datetime1.previous(0, 0, 5, 0 , 0, 0)   
    print(datetime1)                            # 2022/07/31 23:59:59
    datetime1.previous(0, 5, 0, 0 , 0, 0)   
    print(datetime1)                            # 2022/02/28 23:59:59
    datetime1.previous(2, 0, 0, 0 , 0, 0)   
    print(datetime1)                            # 2020/02/28 23:59:59
    datetime1.next(0, 0, 1, 0, 0, 0)   
    print(datetime1)                            # 2020/02/29 23:59:59
    datetime1.next(2, 0, 1, 0, 0, 0)   
    print(datetime1)                            # 2022/03/01 23:59:59