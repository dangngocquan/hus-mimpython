def half_pyramid(number_of_lines):
    for number in range(1, number_of_lines + 1):
        print("*" * number)
    print()
    
def inverted_half_pyramid(number_of_lines):
    for number in range(-number_of_lines, 0):
        print("*" * (-number))
    print()

def hollow_inverted_half_pyramid(number_of_lines):
    for number in range(-number_of_lines, 0):
        if number == -number_of_lines:
            print("*" * (-number))
        else:
            if -number >= 2:
                print('*' + ' ' * (-number - 2) + '*')
            else:
                print('*')
    print()
    
def full_pyramid(number_of_lines):
    for number in range(1, number_of_lines + 1):
        print("{0:^{1}}".format("* " * number, number_of_lines * 2))
    print()
    
def inverted_full_pyramid(number_of_lines):
    for number in range(-number_of_lines, 0):
        print("{0:^{1}}".format("* " * (-number), number_of_lines * 2))
    print()

def hollow_full_pyramid(number_of_lines):
    for number in range(1, number_of_lines + 1):
        temp_string = ""
        if number == 1 or number == number_of_lines:
            temp_string = "* " * number
        else:
            temp_string = "* " + "  " * (number - 2) + "* "
        print("{0:^{1}}".format(temp_string, number_of_lines * 2))
    print()

if __name__ == '__main__':
    # (1) Half Pyramid
    half_pyramid(6)
    # *
    # **
    # ***
    # ****
    # *****
    # ******
    
    # (2) Inverted Half Pyramid
    inverted_half_pyramid(6)
    # ******
    # *****
    # ****
    # ***
    # **
    # *
    
    # (3) Hollow Inverted Half Pyramid
    hollow_inverted_half_pyramid(6)
    # ******
    # *   *
    # *  *
    # * *
    # **
    # *
    
    # (4) Full Pyramid
    full_pyramid(6)
    #      * 
    #     * * 
    #    * * * 
    #   * * * * 
    #  * * * * * 
    # * * * * * * 
     
    # (5) Inverted Full Pyramid
    inverted_full_pyramid(6)
    # * * * * * * 
    #  * * * * * 
    #   * * * * 
    #    * * * 
    #     * * 
    #      * 
     
    # (6) Hollow Full Pyramid
    hollow_full_pyramid(6)
    #      * 
    #     * * 
    #    *   * 
    #   *     * 
    #  *       * 
    # * * * * * *  