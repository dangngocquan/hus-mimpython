"""(a) So sánh vòng lặp do-while trong C++ với vòng lặp while trong Python."""
    # do-while thực hiện khối lệnh ít nhất 1 lần, sau đó mới phụ thuộc vào 
    # điều kiện, còn while thì phụ thuộc hoàn toàn vào điều kiện
    
"""(b) Có thể biến đổi tương đương đoạn code sử dụng do-while trong C++ sang 
đoạn code sử dụng while trong Python hay không?"""
# do-while chỉ khác while ở chỗ là nó thực hiện khối lệnh ít nhất 1 lần. 
# Vì vậy, ta hoàn toàn có thể tạo ra 1 đoạn code sử dụng while trong python 
# có tác dụng tương tự do-while trong C++
# Ví dụ, trong C++, ta có đoạn code:
#   bool condition = false;
#   do {
#       cout << "1";
#   } while (condition);
# Đoạn code trên sẽ có Output là:
#   1
# Ta có thể làm điều tương tự trong python, sử dụng while kết hợp với 1 biến đếm:
#   count = 0
#   condition = False
#   while condition or count < 1:
#       print("1")
#       count += 1
# Đoạn code trên cũng cho ra Output là:
#   1
