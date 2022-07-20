letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
           'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encoding(word, rot_number):
    answer = ""
    for char in word:
        answer += letters[(letters.index(char.upper()) + rot_number) % 26]
    return answer

def decoding(word, rot_number):
    answer = ""
    for char in word:
        answer += letters[(letters.index(char.upper()) - rot_number) % 26]
    return answer

if __name__ == '__main__':
    print(encoding("PYTHON", 19))   # IRMAHG
    print(decoding("IRMAHG", 19))   # PYTHON
    print(encoding("PYTHON", 13))   # CLGUBA
    print(decoding("CLGUBA", 13))   # PYTHON