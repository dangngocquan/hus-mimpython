def listAverage(lst):
    try:
        if type(lst) != type([]):
            raise Exception("The input is not a list.")
        if len(lst) == 0:
            raise Exception("The input list is empty.")
        for number in lst:
            if type(number) != type(0) and type(number) != type(0.1):
                raise Exception("The input list has invalid element.")
        return sum(lst) / len(lst)    
    except Exception as e:
        print(e)
        

if __name__ == '__main__':
    """Testcase 01:"""
    lst = 0
    print(listAverage(lst))
    # The input is not a list.
    # None
    
    """Testcase 02:"""
    lst = []
    print(listAverage(lst))
    # The input list is empty.
    # None
    
    """Testcase 03:"""
    lst = [1, 2.6, "3"]
    print(listAverage(lst))
    # The input list has invalid element.
    # None
    
    """Testcase 04:"""
    lst = [1, 2.6, 3]
    print(listAverage(lst))
    # 2.1999999999999997
