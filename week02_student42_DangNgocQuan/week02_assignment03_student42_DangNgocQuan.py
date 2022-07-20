def get_file_name(student_name, week_number, assignment_number):
    file_name = "week{0:0>2}_assignment{1:0>2}_{2}".format(
                                                    week_number, 
                                                    assignment_number, 
                                                    student_name)
    return file_name

if __name__ == '__main__':
    print(get_file_name("DangNgocQuan", 2, 3))  #week02_assignment03_DangNgocQuan
    print(get_file_name("DangNgocQuan", 2, 4))  #week02_assignment04_DangNgocQuan
    print(get_file_name("DangNgocQuan", 2, 10))  #week02_assignment10_DangNgocQuan