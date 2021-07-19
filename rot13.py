#https://www.codewars.com/kata/530e15517bc88ac656000716/train/python

def rot13(text):
    key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    transform = dict(zip(key, val))
    return ''.join(transform.get(char, char) for char in text) 

print(rot13("test"),"grfg")
print(rot13("Test"),"Grfg")
