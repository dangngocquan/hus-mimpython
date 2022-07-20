# Tic-tac-toe 3x3
# Luật chơi: Bàn cờ 3x3 gồm 9 ô vuông. Hai người chơi thay phiên nhau đánh 
# các dấu X, O vào các ô vuông này. Người thắng cuộc cuối cùng là người có 
# liên tiếp 3 quân ngang, 3 quân dọc hoặc 3 quân chéo mà không bị đối thủ 
# chặn giữa. Nếu không ai thỏa mãn điều kiện đó thì ván đầu được tính là hòa.

# Input:  Đầu vào gồm một số nguyên dương n - tổng số nước đi mà hai người đã 
#         chơi trong ván đấu (1 <= n <= 9).
#         n dòng tiếp theo, mỗi dòng gồm 2 số nguyên không âm r, c ngăn cách 
#         nhau bởi một khoảng trắng, nhằm mô tả tọa độ ô vuông mà người chơi 
#         muốn đánh trong lượt đi của mình.
#         Trong đó:   r - chỉ số của hàng     (0 <= r, c <= 2)
#                     c - chỉ số của cột
                    
# Output: Biết rằng người chơi thứ nhất luôn đi trước và chọn quân X, người 
#         chơi thứ hai luôn đi sau và chọn quân O.
#         Hãy in ra màn hình:
#         "X" nếu người chơi thứ nhất thắng, 
#         "O" nếu người thứ chơi thứ hai thắng. 
#         "-1" nếu ván đấu hòa.

def get_winner(board):
    for row in range(0, 3):
        if (board[row][0] == board[row][1] 
            and board[row][1] == board[row][2] 
            and board[row][2] != 'null'):
            return board[row][0]
    
    for column in range(0, 3):
        if (board[0][column] == board[1][column] 
            and board[1][column] == board[2][column] 
            and board[2][column] != 'null'):
            return board[0][column]
    
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2] 
        and board[1][1] != 'null') or (board[0][2] == board[1][1] 
        and board[1][1] == board[2][0] and board[1][1] != 'null'):
        return board[1][1]
    
    return "-1"  

def play():
    board = [
            ['null', 'null', 'null'], 
            ['null', 'null', 'null'], 
            ['null', 'null', 'null']
            ]
    n = int(input())
    for turn in range(1, n+1):
        temp_list = input().split()
        row = int(temp_list[0])
        column = int(temp_list[1])
        if turn % 2 == 0:
            board[row][column] = 'O'
        else:
            board[row][column] = 'X'
    
    print(get_winner(board))

if __name__ == '__main__':
    play()
    # Match 01:
        # Input:
            # 9
            # 1 1
            # 0 2
            # 0 0
            # 2 2
            # 1 2
            # 1 0
            # 2 1
            # 0 1
            # 2 0
        # Ouput
            # -1
    # Match 02:
        # Input
            # 7
            # 1 1
            # 0 1
            # 2 2
            # 0 0
            # 0 2
            # 2 0
            # 1 2
        # Output:
            # X
            
    # Match 03:
        # Input
            # 6
            # 0 0
            # 1 1
            # 0 1
            # 0 2
            # 1 2
            # 2 0
        # Output
            # O
            
    
    
    