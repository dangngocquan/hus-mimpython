def isSpecialCharacter(ch):
    if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
        return False
    if ord(ch) >= ord('A') and ord(ch) <= ord('Z'):
        return False
    if ord(ch) >= ord('0') and ord(ch) <= ord('9'):
        return False
    return True

def wordVietToEng(word):
    ans = ""
    sign = ""   # Dấu của từ
    mark = ""   # Lưu dấu câu, các kí tự đặc biệt
    for ch in word.lower():
        if ch in vietToEng.keys():
            ans += vietToEng[ch]
        elif isSpecialCharacter(ch):
            mark += ch
        else:
            ans += ch
        if ch in signs.keys():
            sign = signs[ch]
        
    return ans + sign + mark

def stringVietToEng(words):
    lst = words.split()
    ans = ""
    for i in range(len(lst)):
        ans += wordVietToEng(lst[i]) + " "
    return ans

def wordEngToViet(word):
    mark = ""
    while len(word) > 0 and isSpecialCharacter(word[-1]):
        mark = word[-1] + mark
        word = word[:len(word)-1]
    
    sign = ""
    if len(word) > 0 and word[-1] in "sfrxj":
        sign = word[-1]
        word = word[:len(word)-1]

    newWord1 = word + ""
    for i in range(len(word)-1):
        if word[i:i+2] in engToViet.keys():
            newWord1 = newWord1.replace(word[i:i+2], engToViet[word[i:i+2]])
            
    newWord2 = newWord1 + ""
    tempListValue = []
    for i in range(len(newWord1)):
        if (newWord1[i] + sign) in engToViet.keys():
            tempListValue.append(newWord1[i])
    if len(tempListValue) > 0:
        newWord2 = newWord2.replace(tempListValue[(len(tempListValue) + 1)//2 - 1], 
                                    engToViet[tempListValue[(len(tempListValue)+1)//2 - 1] + sign])
    return newWord2 + mark

def stringEngToViet(words):
    ans = ""
    lst = words.split()
    for i in range(len(lst)):
        ans += wordEngToViet(lst[i]) + " "
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
    
    engToViet = {
        'aa' : 'â',
        'aw' : 'ă',
        'dd' : 'đ',
        'ee' : 'ê',
        'oo' : 'ô',
        'ow' : 'ơ',
        'uw' : 'ư',
        'as' : 'á',
        'af' : 'à',
        'ar' : 'ả',
        'ax' : 'ã',
        'aj' : 'ạ',
        'âs' : 'ấ',
        'âf' : 'ầ',
        'âr' : 'ẩ',
        'âx' : 'ẩ',
        'âj' : 'ậ',
        'ăs' : 'ắ',
        'ăf' : 'ằ',
        'ăr' : 'ẳ',
        'ăx' : 'ẵ',
        'ăj' : 'ặ',
        'es' : 'é',
        'ef' : 'è',
        'er' : 'ẻ',
        'ex' : 'ẽ',
        'ej' : 'ẹ',
        'ês' : 'ế',
        'êf' : 'ề',
        'êr' : 'ể',
        'êx' : 'ễ',
        'êj' : 'ệ',
        'is' : 'í',
        'if' : 'ì',
        'ir' : 'ỉ',
        'ix' : 'ĩ',
        'ij' : 'ị',
        'os' : 'ó',
        'of' : 'ò',
        'or' : 'ỏ', 
        'ox' : 'õ', 
        'oj' : 'ọ',
        'ôs' : 'ố',
        'ôf' : 'ồ',
        'ôr' : 'ổ',
        'ôx' : 'ỗ',
        'ôj' : 'ộ',
        'ơs' : 'ớ',
        'ơf' : 'ờ',
        'ơr' : 'ở',
        'ơx' : 'ỡ',
        'ơj' : 'ợ',
        'us' : 'ú',
        'uf' : 'ù',
        'ur' : 'ủ',
        'ux' : 'ũ',
        'uj' : 'ụ',
        'ưs' : 'ứ',
        'ưf' : 'ừ',
        'ưr' : 'ử',
        'ưx' : 'ữ',
        'ưj' : 'ự',
        'ys' : 'ý',
        'yf' : 'ỳ',
        'yr' : 'ỷ',
        'yx' : 'ỹ',
        'yj' : 'ỵ'
    }
    
    print(stringVietToEng('''Câu văn này chỉ mang tính chất minh họa, nhưng nó đã thực hiện 
                          được nhiệm vụ mà nó cần thực hiện, đó là minh họa =)).'''))
    # caau vawn nayf chir mang tinhs chaats minh hoaj, nhuwng nos ddax thuwcj hieenj 
    # dduwowcj nhieemj vuj maf nos caanf thuwcj hieenj, ddos laf minh hoaj =)).
    
    print(stringEngToViet("Kieems nguwowif yeeu ddi nhes!!!"))
    # Kíêm người yêu đi nhé!!!
    
    print(stringEngToViet('''caau vawn nayf chir mang tinhs chaats minh hoaj, nhuwng nos ddax 
                          thuwcj hieenj dduwowcj nhieemj vuj maf nos caanf thuwcj hieenj, ddos 
                          laf minh hoaj =)).'''))
    # câu văn này chỉ mang tính chất minh họa, nhưng nó đã thực hịên đựơc nhịêm vụ mà nó cần thực 
    # hịên, đó là minh họa =)).
    