# Viết một chương trình giải quyết một bài tập hình học cơ bản.
# Yêu cầu đối với bài tập:
#     + Các thư viện hình học (class Point, class Line, class Circle, …) cần được đặt bên trong thư mục 
#     additionalFolder/. (Nên) sử dụng relative import giữa các file Python.
#     + Trong file chính, import các thư viện hình học (sử dụng absolute import), đồng thời trình bày rõ 
#     cấu trúc thư mục trong phần docstrings.

"""
additionalFolder
    assignment03
        geometry.py
        point.py
        line.py
        circle.py
week07_assignment03_student42_DangNgocQuan.py
"""

from additionalFolder.assignment03.geometry import Point, Circle, Line

if __name__ == '__main__':
    circle = Circle(center=Point(0, 0), radius=5)
    print(circle.area())    # 78.53981633974483