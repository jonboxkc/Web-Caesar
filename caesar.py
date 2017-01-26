def alphabet_position(letter):
    if letter.isupper():
        result = ord(letter) - ord("A")
    elif letter.islower():
        result = ord(letter) - ord("a")
    else:
        return(letter)
    return result

def rotate_character(char, rot):
    rot=int(rot)
    if rot > 26:
            rot = rot % 26
    for i in char:
        if i.isalpha():
            if i.isupper():
                newPos = rot + ord(char)
                if newPos in range(65,91):
                    return chr(newPos)
                else:
                    fixPos = newPos - 26
                    fixLett = chr(fixPos)
                    return fixLett
            else:
                newPos = rot + ord(char)
            if newPos in range(65,90):
                return chr(newPos)
            elif newPos in range(97,123):
                return chr(newPos)
            else:
                fixPos = newPos - 26
                fixLett = chr(fixPos)
                return fixLett
        else:
            return char

def encrypt(text, rot):
        text = str(text)
        newTExt = ""
        for char in text:
            newTExt = newTExt + rotate_character(char,rot)
        return newTExt
