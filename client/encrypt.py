def encrypt_transpose(s):
    txt = ""
    for sentence in s.split('\n'):
        for word in sentence.split():
            txt = txt + word[::-1] + ' '
        txt = txt.strip()
        txt = txt + '\n'

    txt = txt.strip()
    return txt

def encrypt_substitute(s):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    lowercase_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    uppercase_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    shift = 2
    txt = ""
    for sentence in s.split('\n'):
        for word in sentence.split():
            # print("-------",type(word))
            # print(len(word))
            for letter in word:
                # print("-----",type(letter))
                if letter in numbers:
                    idx = numbers.index(letter)        
                    idx += shift
                    idx = idx%10
                    txt = txt + numbers[idx]
                
                elif letter in lowercase_letters:
                    idx = lowercase_letters.index(letter)        
                    idx += shift
                    idx = idx%26
                    txt = txt + lowercase_letters[idx]

                elif letter in uppercase_letters:
                    idx = uppercase_letters.index(letter)        
                    idx += shift
                    idx = idx%26
                    txt = txt + uppercase_letters[idx]
            
                else:
                    txt = txt + letter

            txt = txt + ' '

        txt = txt.strip()
        txt = txt + '\n'

    txt = txt.strip() 
    return txt