import numpy

def function1d(array):
    return numpy.repeat(array, 2)

if __name__ == '__main__':
    '''Nêu ý nghĩa của hàm, cho ví dụ.'''
    
    '''1. numpy.array()'''  # Tạo mảng trong numpy với list dữ liệu có sẵn
    matrix = numpy.array([[1, 2, 3], [4, 5, 6]])
    print(matrix)
    # [[1 2 3]
    #  [4 5 6]]
    
    '''2. numpy.mean() '''    # Lấy trung bình cộng
    print(numpy.mean(matrix))   # Lấy trung bình cộng của tất cả các phần tử trong mảng 
    # 3.5 
    print(numpy.mean(matrix, axis=0)) # Lấy trung bình cộng theo chiều đầu tiên
    # [2.5 3.5 4.5]
    print(numpy.mean(matrix, axis=1)) # Lấy trung bình cộng theo chiều thứ hai
    # [2. 5.]
    
    '''3. numpy.median() '''  # Lấy trung bình cộng
    print(numpy.median(matrix)) # Lấy trung bình cộng của tất cả các phần tử trong mảng 
    # 3.5
    print(numpy.median(matrix, axis=0)) # Lấy trung bình cộng theo chiều đầu tiên
    # [2.5 3.5 4.5]
    print(numpy.median(matrix, axis=1)) # Lấy trung bình cộng theo chiều thứ hai
    # [2. 5.]
    
    '''4. numpy.max() '''   # Giá trị lớn nhất
    print(numpy.max(matrix))    # Lấy giá trị lớn nhất của mảng
    # 6
    print(numpy.max(matrix, axis=0))    # Lấy giá trị lớn nhất theo chiều đầu tiên
    #[4 5 6]
    print(numpy.max(matrix, axis=1))    # Lấy giá trị lớn nhất theo chiều thứ hai
    # [3 6]
    
    '''5. numpy.min() '''   # Giá trị nhỏ nhất
    print(numpy.min(matrix))    # Lấy giá trị nhỏ nhất của mảng
    # 1
    print(numpy.min(matrix, axis=0))    # Lấy giá trị nhỏ nhất theo chiều đầu tiên
    #[1 2 3]
    print(numpy.min(matrix, axis=1))    # Lấy giá trị nhỏ nhất theo chiều thứ hai
    # [1 4]
    
    '''6. numpy.argmax() '''    # Chỉ số của phần tử lớn nhất
    print(numpy.argmax(matrix)) # Chỉ số của phần tử lớn nhất trong mảng
    # 5
    print(numpy.argmax(matrix, axis=0)) # Chỉ số của các phần tử lớn nhất theo chiều thứ nhất
    # [1 1 1]
    print(numpy.argmax(matrix, axis=1)) # Chỉ số của các phần tử lớn nhất theo chiều thứ hai
    # [2 2]
    
    '''7. numpy.argmin() '''    # Chỉ số của phần tử nhỏ nhất
    print(numpy.argmin(matrix)) # Chỉ số của phần tử nhỏ nhất trong mảng
    # 0
    print(numpy.argmin(matrix, axis=0)) # Chỉ số của các phần tử nhỏ nhất theo chiều thứ nhất
    # [0 0 0]
    print(numpy.argmin(matrix, axis=1)) # Chỉ số của các phần tử nhỏ nhất theo chiều thứ hai
    # [0 0]
    
    '''8. numpy.arange() '''    # Tạo mảng một chiều, có start, stop và step
    print(numpy.arange(5, 18, 2))   # Tạo mảng một chiều, có start = 5, stop = 18, step = 2
    # [ 5  7  9 11 13 15 17]
    
    '''9. numpy.linspace() ''' # Tạo mảng một chiều, có start, stop và num (mặc định = 50)
    print(numpy.linspace(3, 15, 5)) # Tạo mảng một chiều, start = 3, stop = 16, num = 5
    # [ 3.  6.  9. 12. 15.]
    
    '''10. numpy.random '''     # Tạo mảng với giá trị random, với kích thước cho sẵn
    print(numpy.random.randint(10, size=(2, 3)))   # Tạo mảng 2 chiều, có 2 hàng, 3 cột với các 
                                                   # giá trị nguyên dương bất kỳ < 10
    # [[4 4 8]
    #  [0 1 0]]
    
    '''11. numpy.repeat'''  # Lặp lại mảng nào đó 1 số lần
    print(numpy.repeat(matrix, 3))  # Lặp lại các phần tử trong matrix 3 lần
    # [1 1 1 2 2 2 3 3 3 4 4 4 5 5 5 6 6 6]
    print(numpy.repeat(matrix, 3, axis=0))  # Lặp lại matrix 3 lần theo chiều thứ nhất
    # [[1 2 3]
    #  [1 2 3]
    #  [1 2 3]
    #  [4 5 6]
    #  [4 5 6]
    #  [4 5 6]]
    print(numpy.repeat(matrix, 3, axis=1))  # Lặp lại matrix 3 lần theo chiều thứ hai
    # [[1 1 1 2 2 2 3 3 3]
    #  [4 4 4 5 5 5 6 6 6]]
    
    '''12. numpy.all '''    # Kiểm tra xem  các phần tử trong mảng có thỏa mãn điều kiện nào đó không
    print(numpy.all(matrix > 0))    # Kiểm tra xem các phần tử của matrix có lớn hơn 0 không
    # True
    print(numpy.all(matrix > 2))    # Kiểm tra xem các phần tử của matrix có lớn hơn 2 không
    # False
    print(numpy.all(matrix > 2, axis=0))    # Kiểm tra xem các phần tử của matrix có lớn hơn 2 không (theo chiều thứ nhất)
    # [False False  True]
    print(numpy.all(matrix > 2, axis=1))    # Kiểm tra xem các phần tử của matrix có lớn hơn 2 không (theo chiều thứ hai)
    # [False  True]
    
    '''13. numpy.any '''    # Kiểm tra xem trong matrix có phần tử nào thỏa mãn điều kiện hay không
    print(numpy.any(matrix > 0))    # Kiểm tra xem có phần tử nào của matrix lớn hơn 0 không
    # True
    print(numpy.any(matrix > 2))    # Kiểm tra xem có phần tử nào của matrix lớn hơn 2 không
    # True
    print(numpy.any(matrix > 2, axis=0))    # Kiểm tra xem có phần tử của matrix lớn hơn 2 không (theo chiều thứ nhất)
    # [ True  True  True]
    print(numpy.any(matrix > 2, axis=1))    # Kiểm tra xem có phần tử của matrix lớn hơn 2 không (theo chiều thứ nhất)
    # [ True  True]
    
    '''14. numpy.ones '''   # Tạo ra mảng gồm những phần tử có giá trị 1
    print(numpy.ones(shape=(2, 3)))
    # [[1. 1. 1.]
    #  [1. 1. 1.]]
    
    '''15. numpy.zeros'''   # Tạo ra mảng gồm những phần tử có giá trị 0
    print(numpy.zeros(shape=(2, 3)))
    # [[0. 0. 0.]
    #  [0. 0. 0.]]
    
    '''16. numpy.savetxt '''    # Lưu dữ liệu vào file txt
    numpy.savetxt(".\\week06_student42_DangNgocQuan\\additionalFolder\\asignment02\\numpySavetxt.txt", 
                  matrix, fmt="%d", delimiter=',', newline='\n')
    # Lưu matrix vào additionalFolder\\asignment02\\numpySavetxt.txt
    
    '''17. numpy.loadtxt '''    # Đọc dữ liệu từ file txt
    print(numpy.loadtxt(".\\week06_student42_DangNgocQuan\\additionalFolder\\asignment02\\numpySavetxt.txt",
                        dtype=int, delimiter=","))
    # [[1 2 3]
    #  [4 5 6]]
    
    '''18. numpy.apply_along_axis ''' # Thay đổi mỗi mảng một chiều của mảng cho trước, theo một function nào đó
    print(matrix)
    # [[1 2 3]
    #  [4 5 6]]
    print(numpy.apply_along_axis(function1d, 0, matrix))
    # [[1 2 3]
    #  [1 2 3]
    #  [4 5 6]
    #  [4 5 6]]
    
    '''18. numpy.where'''   # Kiểm tra các phần tử của mảng theo một điều kiện nào đó, và thay thế chúng nếu cần
    print(numpy.where(matrix >2, matrix, 0))    # Kiểm tra xem phần tử có > 2 hay không, nếu có thì giữ nguyên, nếu không thì
                                                # thay thế = 0
    # [[0 0 3]
    #  [4 5 6]]
    
    '''19. numpy.isclose '''    # Kiểm tra xem các phần tử của 2 mảng có "gần" nhau không
    array1 = numpy.array([1, 6, 13, 19])
    array2 = numpy.array([0, 3, 12, 21])
    print(numpy.isclose(array1, array2, atol=2))
    # [ True False  True  True]
    
    
    '''Viết chương trình thực hiện đúng ý nghĩa đó mà hạn chế sử dụng thư viện numpy. Có thể sử dụng 
    thư viện để khởi tạo mảng số nếu cần thiết.'''
    
    
    '''So sánh tốc độ thực thi giữa hai cách làm: phương pháp thủ công và phương pháp sử dụng numpy.'''
    # Tốc độ thực thi khi sử dụng hàm numpy nhanh hơn nhiều so với phương pháp thủ công.