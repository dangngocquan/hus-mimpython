def winner(firstChoice, secondChoice):
    if firstChoice == secondChoice:
        return -1
    if (firstChoice - secondChoice == 1) or (firstChoice - secondChoice == -2):
        return 1
    return 2

if __name__ == '__main__':
    """ (a) Viết một chương trình để hai người có thể chơi trò chơi kéo - búa - bao với nhau. """
    # Ta định nghĩa:  "Kéo" tương ứng với 0
    #                 "Búa" tương ứng với 1
    #                 "Bao" tương ứng với 2
    # Input:  Dòng đầu tiên sẽ là một số nguyên (0, 1 hoặc 2) tương ứng với lựa chọn của người chơi thứ nhất.
    #         Dòng thứ hai sẽ là một số nguyên (0, 1 hoặc 2) tương ứng với lựa chọn của người chơi thứ hai.
    # Output: In ra '1' nếu người chơi thứ nhất thắng.
    #         In ra '2' nếu người chơi thứ hai thắng.
    #         In ra '-1' nếu hai người chơi hòa.
    print(winner(0, 1))     # 2
    print(winner(0, 2))     # 1
    print(winner(2, 1))     # 1
    print(winner(1, 2))     # 2
    print(winner(0, 0))     # -1
    
    
    """(b) Cách tiếp cận đơn giản là cho phép hai người chơi A, B lần lượt đưa ra lựa chọn và nhập nó vào 
    chương trình thông qua bàn phím (giả sử A nhập trước). Cách chơi như vậy không công bằng vì ở mỗi 
    lượt chơi B luôn biết được lựa chọn của A trước khi B đưa ra lựa chọn. Thiết kế chương trình để đảm 
    bảo tính công bằng cho trò chơi. """
    # Ta sẽ đồng thời cho hai người chơi viết các lựa chọn của mình, và lưu nó vào hai file riêng biệt, 
    # có thể đảm bảo rằng người này không nhìn được sự lựa chọn của người kia, việc chọn lựa của hai 
    # người chơi là xảy ra cùng lúc.
    # Input:    Giả sử ta có được hai file: player01.txt và player02.txt lần lượt là các file lưu trữ 
    #           các lựa chọn tương ứng với người chơi thứ nhất và người chơi thứ hai, mỗi file chứa đúng 
    #           n dòng (n > 0), mỗi dòng chứa duy nhất một số nguyên 0, 1 hoặc 2.
    # Output:   In ra n dòng, mỗi dòng chứa 1 số nguyên:
    #               + In ra '1' nếu người chơi thứ nhất thắng.
    #               + In ra '2' nếu người chơi thứ hai thắng.
    #               + In ra '-1' nếu hai người chơi hòa.
    
    # Example: 
    
    #   player01.txt có nội dung như sau:
    #   1
    #   2
    #   0
    #   2
    #   1
    #   0
    #   2
    #   0
    
    #   player02.txt có nội dung như sau:
    #   2
    #   1
    #   0
    #   2
    #   0
    #   0
    #   1
    #   2
    
    firstPlayerChoices = []
    secondPlayerChoices = []
    
    with open("Files\\week03_assignment05\\player01.txt", 'r') as f:
        firstPlayerChoices = f.read().splitlines()
        f.close()
    with open("Files\\week03_assignment05\\player02.txt", 'r') as f:
        secondPlayerChoices = f.read().splitlines()
        f.close()
    
    for index in range(len(firstPlayerChoices)):
        print(winner(int(firstPlayerChoices[index]),
                     int(secondPlayerChoices[index])))
    
    #   Output:
    #   2
    #   1
    #   -1
    #   -1
    #   1
    #   -1
    #   1
    #   1
    
    
    """(c) Có thể hiểu tính công bằng theo nghĩa nào khác?"""
    # Ta có thể hiểu tính công bằng theo một nghĩa khác. Chẳng hạn như: hai người chơi đều nên tuân thủ 
    # đúng luật chơi, một trong hai không thể phá luật được: 'Kéo' không thể thắng 'Búa', 'Bao' không
    # thể thắng 'Kéo', ... Hoặc cũng có thể theo một nghĩa khác: Sau khi người chơi đã đưa ra lựa chọn, họ không thể 
    # thay đổi lựa chọn được nữa.
    
    
    
    
