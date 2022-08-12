def wordVietToEng(word):
    ans = ""
    sign = ""
    mark = ""
    for ch in word.lower():
        if ch in vietToEng.keys():
            ans += vietToEng[ch]
        elif not ((ord(ch) >= ord('a') and ord(ch) <= ord('z')) or 
                  (ord(ch) >= ord('0') and ord(ch) <= ord('9'))):
            mark += ch
        else:
            ans += ch
        if ch in signs.keys():
            sign = signs[ch]
        
    return ans + sign + mark

def stringVietToEng(words):
    ans = words.split()
    for i in range(len(ans)):
        ans[i] = wordVietToEng(ans[i])
    ans = " ".join(ans)
    return ans
        

if __name__ == '__main__':
    vietToEng = {
        'á' : 'a',
        'à' : 'a',
        'ả' : 'a',
        'ã' : 'a',
        'ạ' : 'a',
        'â' : 'aa',
        'ấ' : 'aa',
        'ầ' : 'aa',
        'ẩ' : 'aa',
        'ẫ' : 'aa',
        'ậ' : 'aa',
        'ă' : 'aw',
        'ắ' : 'aw',
        'ằ' : 'aw',
        'ẳ' : 'aw',
        'ẵ' : 'aw',
        'ặ' : 'aw',
        'đ' : 'dd',
        'é' : 'e',
        'è' : 'e',
        'ẻ' : 'e',
        'ẽ' : 'e',
        'ẹ' : 'e',
        'ê' : 'ee',
        'ế' : 'ee',
        'ề' : 'ee',
        'ể' : 'ee',
        'ễ' : 'ee',
        'ệ' : 'ee',
        'í' : 'i',
        'ì' : 'i',
        'ỉ' : 'i',
        'ĩ' : 'i',
        'ị' : 'i',
        'ó' : 'o',
        'ò' : 'o',
        'ỏ' : 'o',
        'õ' : 'o',
        'ọ' : 'o',
        'ô' : 'oo',
        'ố' : 'oo',
        'ồ' : 'oo',
        'ổ' : 'oo',
        'ỗ' : 'oo',
        'ộ' : 'oo',
        'ơ' : 'ow',
        'ớ' : 'ow',
        'ờ' : 'ow',
        'ở' : 'ow',
        'ỡ' : 'ow',
        'ợ' : 'ow',
        'ú' : 'u',
        'ù' : 'u',
        'ủ' : 'u',
        'ũ' : 'u',
        'ụ' : 'u',
        'ư' : 'uw',
        'ứ' : 'uw',
        'ừ' : 'uw',
        'ử' : 'uw',
        'ữ' : 'uw',
        'ự' : 'uw',
        'ý' : 'y',
        'ỳ' : 'y',
        'ỷ' : 'y',
        'ỹ' : 'y',
        'ỵ' : 'y',
    }
    
    signs = {
        'á' : 's',
        'à' : 'f',
        'ả' : 'r',
        'ã' : 'x',
        'ạ' : 'j',
        'ấ' : 's',
        'ầ' : 'f',
        'ẩ' : 'r',
        'ẫ' : 'x',
        'ậ' : 'j',
        'ắ' : 's',
        'ằ' : 'f',
        'ẳ' : 'r',
        'ẵ' : 'x',
        'ặ' : 'j',
        'é' : 's',
        'è' : 'f',
        'ẻ' : 'r',
        'ẽ' : 'x',
        'ẹ' : 'j',
        'ế' : 's',
        'ề' : 'f',
        'ể' : 'r',
        'ễ' : 'x',
        'ệ' : 'j',
        'í' : 's',
        'ì' : 'f',
        'ỉ' : 'r',
        'ĩ' : 'x',
        'ị' : 'j',
        'ó' : 's',
        'ò' : 'f',
        'ỏ' : 'r',
        'õ' : 'x',
        'ọ' : 'j',
        'ố' : 's',
        'ồ' : 'f',
        'ổ' : 'r',
        'ỗ' : 'x',
        'ộ' : 'j',
        'ớ' : 's',
        'ờ' : 'f',
        'ở' : 'r',
        'ỡ' : 'x',
        'ợ' : 'j',
        'ú' : 's',
        'ù' : 'f',
        'ủ' : 'r',
        'ũ' : 'x',
        'ụ' : 'j',
        'ứ' : 's',
        'ừ' : 'f',
        'ử' : 'r',
        'ữ' : 'x',
        'ự' : 'j',
        'ý' : 's',
        'ỳ' : 'f',
        'ỷ' : 'r',
        'ỹ' : 'x',
        'ỵ' : 'j',
    }
    
    print(stringVietToEng('''Câu văn này chỉ mang tính chất minh họa, nhưng nó đã thực hiện 
                          được nhiệm vụ mà nó cần thực hiện, đó là minh họa =)).'''))
    # caau vawn nayf chir mang tinhs chaats minh hoaj, nhuwng nos ddax thuwcj hieenj 
    # dduwowcj nhieemj vuj maf nos caanf thuwcj hieenj, ddos laf minh hoaj =)).
    