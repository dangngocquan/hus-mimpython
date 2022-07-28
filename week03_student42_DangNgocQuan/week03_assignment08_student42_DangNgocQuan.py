import maskpass
import re

def isSamePassword(password, confirmPassword):
    return password == confirmPassword

def hasValidLength(password, minLength):
    return len(password) >= minLength\
        
def hasDigitCharacter(password):
    return re.search("[0-9]", password) != None

def hasUpperCharacter(password):
    return re.search("[A-Z]", password) != None

def hasLowerCharacter(password):
    return re.search("[a-z]", password) != None

def hasSpecialCharacter(password):
    return re.search("[^0-9a-zA-Z]", password) != None

def isStrongPassword(password):
    # Dài ít nhất 12 ký tự. Mật khẩu càng dài - càng tốt.
    # Sử dụng chữ hoa và chữ thường, số và các ký hiệu đặc biệt.
    if not hasValidLength(password, 12):
        print("Mật khẩu cần có ít nhất 12 kí tự! Hãy thử lại.")
        return False
    if not hasDigitCharacter(password):
        print("Mật khẩu cần có ít nhất 1 chữ số! Hãy thử lại.")
        return False
    if not hasLowerCharacter(password):
        print("Mật khẩu cần có ít nhất 1 kí tự chữ thường! Hãy thử lại.")
        return False
    if not hasUpperCharacter(password):
        print("Mật khẩu cần có ít nhất 1 kí tự chữ hoa! Hãy thử lại.")
        return False
    if not hasSpecialCharacter(password):
        print("Mật khẩu cần có it nhất 1 kí tự đặc biệt! Hãy thử lại.")
        return False
    return True

def register():
    username = input("Username: ")
    password = ""
    confirmPassword = " "
    while password != confirmPassword or not isStrongPassword(password):
        password = maskpass.advpass("Password: ", "*")
        confirmPassword = maskpass.advpass("Confirm Password: ", "*")
        if not isSamePassword(password, confirmPassword):
            print("Xác nhận mật khẩu không khớp! Hãy thử lại.")
    print("Bạn đã đăng kí tài khoản thành công!")
    return {"username" : username,
            "password" : password}

if __name__ == '__main__':
    accounts = []
    account = register()
    accounts.append(account)
    print(accounts)
    # Đây là 1 đoạn input nhập từ bàn phím và output tương ứng
    # Username: dangngocquan
    # Password: *****           12345
    # Confirm Password: ****    1234
    # Xác nhận mật khẩu không khớp! Hãy thử lại.
    # Password: *****           12345
    # Confirm Password: *****   12345
    # Mật khẩu cần có ít nhất 12 kí tự! Hãy thử lại.
    # Password: ************            123456789012
    # Confirm Password: ************    123456789012
    # Mật khẩu cần có ít nhất 1 kí tự chữ thường! Hãy thử lại.
    # Password: ************            a12345678901
    # Confirm Password: ************    a12345678901
    # Mật khẩu cần có ít nhất 1 kí tự chữ hoa! Hãy thử lại.
    # Password: ************            aA1234567890
    # Confirm Password: ************    aA1234567890
    # Mật khẩu cần có it nhất 1 kí tự đặc biệt! Hãy thử lại.
    # Password: ************            aA@123456789
    # Confirm Password: ************    aA@123456789
    # Bạn đã đăng kí tài khoản thành công!
    # [['dangngocquan', 'aA@123456789']]

    
    
    